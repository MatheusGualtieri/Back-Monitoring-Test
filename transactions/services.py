from transactions.serializers import SendEmailSerializer
from .models import Transaction
from avg_graphs.models import AvgGraph
from avg_graphs.serializers import AvgGraphSerializer
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings


class MonitoringSystem:
    @staticmethod
    def get_avg(values, divisor=1):
        total = 0
        for item in values:
            total = total + item["count"]
        return total / divisor

    @staticmethod
    def group_by_hour(transactions):
        transactions_by_hour = {}
        for transaction in transactions:
            time_helper = transaction["time"].replace(":", " ").split()
            for i in range(0, 24):
                if int(time_helper[0]) == i:
                    list_helper = transactions_by_hour.get(f"{i}", [])
                    list_helper.append(transaction)
                    transactions_by_hour[f"{i}"] = list_helper
                    break
        return transactions_by_hour

    @staticmethod
    def group_by_status(data):
        transactions_by_status = {}

        for transaction in data:
            list_helper = transactions_by_status.get(f"{transaction['status']}", [])
            list_helper.append(transaction)
            transactions_by_status[f"{transaction['status']}"] = list_helper
        return transactions_by_status

    @staticmethod
    def generate_graph_info(start=None, finish=None, data=None):
        graph_info = {f"{indice}": [] for indice in range(0, 24)}
        if data:
            group_by_hour = MonitoringSystem.group_by_hour(data)
            for key, value in group_by_hour.items():
                graph_info[f"{key}"] = MonitoringSystem.group_by_status(value)
        else:
            new_data = Transaction.objects.filter(date__range=(start, finish))
            group_by_hour = MonitoringSystem.group_by_hour(new_data)
            for key, value in group_by_hour.items():
                graph_info[f"{key}"] = MonitoringSystem.group_by_status(value)

        graph_info_avg = {f"{indice}": {} for indice in range(0, 24)}
        for key, value in graph_info.items():
            count_helper = 0
            for item in value:
                count_helper = MonitoringSystem.get_avg(value[item], 60)
                graph_info_avg[key][item] = count_helper
        for key, value in graph_info_avg.items():
            count_helper = 0
            for item in value:
                if item != "approved" and item != "total_not_approved":
                    count_helper = count_helper + value[item]
            graph_info_avg[key]["total_not_approved"] = count_helper

        return graph_info_avg
        # guardar as informacoes na tabela do grafico

    @staticmethod
    def check_anomalies(data, email):
        graph_info_new_data = MonitoringSystem.generate_graph_info(data=data)
        graph_today_approved = {f"{indice}": {} for indice in range(0, 24)}
        graph_today_not_approved = {f"{indice}": {} for indice in range(0, 24)}
        for key, value in graph_info_new_data.items():
            for item in value:
                if item == "approved":
                    graph_today_approved[key][item] = value[item]
                elif item == "total_not_approved":
                    graph_today_not_approved[key][item] = value[item]
        # base_graph_data = AvgGraph.objects.filter(is_base__iexact=True)
        base_graph_info = {
            "0": {"approved": 4.885},
            "1": {"approved": 1.92},
            "2": {"approved": 0.8},
            "3": {"approved": 0.46},
            "4": {"approved": 0.21},
            "5": {"approved": 0.73},
            "6": {"approved": 2.19},
            "7": {"approved": 5.12},
            "8": {"approved": 10.12},
            "9": {"approved": 18.355},
            "10": {"approved": 28.46},
            "11": {"approved": 28.39},
            "12": {"approved": 28.39},
            "13": {"approved": 24.19},
            "14": {"approved": 25.05},
            "15": {"approved": 27.745},
            "16": {"approved": 25.585},
            "17": {"approved": 22.475},
            "18": {"approved": 18.37},
            "19": {"approved": 18.44},
            "20": {"approved": 18.725},
            "21": {"approved": 17.695},
            "22": {"approved": 15.57},
            "23": {"approved": 8.75},
        }
        # base_graph_info = MonitoringSystem.generate_graph_info(base_graph_data)
        # falta comparar a média de erros desses dados, com a média de erros do grafico base
        for key, value in graph_info_new_data.items():
            for item in value:
                verify_errors = item.lower().split("_")
                for status in verify_errors:
                    if status == "backend":
                        MonitoringSystem.alert(
                            "_".join(verify_errors),
                            value[item],
                            email,
                            "O problema é ainda maior, pois o erro é no Backend",
                        )
                if (
                    item != "approved"
                    and value[item] > graph_today_approved[key].get("approved", 0)
                    or value[item] > base_graph_info[key]["approved"]
                ):
                    MonitoringSystem.alert(item, value[item], email)
                if (
                    graph_today_not_approved[key]["total_not_approved"]
                    > graph_today_approved[key].get("approved", 0)
                    or graph_today_not_approved[key]["total_not_approved"]
                    > base_graph_info[key]["approved"]
                ):
                    MonitoringSystem.alert(
                        "total_not_approved",
                        graph_today_not_approved[key]["total_not_approved"],
                        email,
                    )
                    break

    @staticmethod
    def alert(status, count, email, extra_msg=""):
        data = {
            "subject": f"Alerta: Quantidade de Transaferências {status} fora do normal",
            "message": f"Alerta, a quantidade de transferencias {status} está fora do normal, estando em media {count}. {extra_msg}",
            "recipient_list": [email],
        }
        serializer = SendEmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        print(data)
        send_mail(
            **serializer.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False,
        )
