from flask import Flask, Response
app = Flask(__name__)


@app.route("/pass/admin/api.php")
def passResponse():
    dict = '{"domains_being_blocked":125230,"dns_queries_today":13322,"ads_blocked_today":5490,"ads_percentage_today":41.21003,"unique_domains":928,"queries_forwarded":6702,"queries_cached":1130,"clients_ever_seen":4,"unique_clients":4,"dns_queries_all_types":13322,"reply_NODATA":12,"reply_NXDOMAIN":15,"reply_CNAME":173,"reply_IP":317,"privacy_level":0,"status":"enabled"}'
    return Response(dict, status=200)

@app.route("/no_status/admin/api.php")
def no_status():
    dict = '{"domains_being_blocked":125230,"dns_queries_today":13322,"ads_blocked_today":5490,"ads_percentage_today":41.21003,"unique_domains":928,"queries_forwarded":6702,"queries_cached":1130,"clients_ever_seen":4,"unique_clients":4,"dns_queries_all_types":13322,"reply_NODATA":12,"reply_NXDOMAIN":15,"reply_CNAME":173,"reply_IP":317,"privacy_level":0}'
    return Response(dict, status=200)

@app.route("/bad_status/admin/api.php")
def bad_status():
    dict = '{"domains_being_blocked":125230,"dns_queries_today":13322,"ads_blocked_today":5490,"ads_percentage_today":41.21003,"unique_domains":928,"queries_forwarded":6702,"queries_cached":1130,"clients_ever_seen":4,"unique_clients":4,"dns_queries_all_types":13322,"reply_NODATA":12,"reply_NXDOMAIN":15,"reply_CNAME":173,"reply_IP":317,"privacy_level":0,"status":"running"}'
    return Response(dict, status=200)

@app.route("/fail/admin/api.php")
def FailResponse():
    dict = '{"domains_being_blocked":125230,"dns_queries_today":13322,"ads_blocked_today":5490,"ads_percentage_today":41.21003,"unique_domains":928,"queries_forwarded":6702,"queries_cached":1130,"clients_ever_seen":4,"unique_clients":4,"dns_queries_all_types":13322,"reply_NODATA":12,"reply_NXDOMAIN":15,"reply_CNAME":173,"reply_IP":317,"privacy_level":0,"status":"enabled"}'
    return Response(dict, status=404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
