from requests_html import HTML, HTMLSession

XPATH = "/html/body/div/table[1]/tbody/tr/tud/table/tbody/tr[1]/td[2]"
BASE_URL = "https://sig.unb.br/sigaa/relatorioProcessamento?idTurma"

id_turma = 1146263

response_html = HTMLSession().get(f"{BASE_URL}={id_turma}").html
# component = response_html.xpath(XPATH, first=True).text.splitlines()
# print(component)

print(response_html)