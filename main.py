
import os


def createTicket(header, body):
    return """curl 'https://ef-hult.freshservice.com/support/tickets' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-GB,en;q=0.5' --compressed -H 'Referer: https://ef-hult.freshservice.com/support/tickets/new' -H 'Content-Type: multipart/form-data; boundary=---------------------------69017500537167808881873478305' -H 'Origin: https://ef-hult.freshservice.com' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: _x_m=x_n; helpdesk_node_session=89557ffb119d700fc51744309d7192f0180d0439d577992661fb534ed45c21a5a8ed2e6492289561cfef4c6112f44c70720764b17909cc3de1126690d1a9c19a; user_credentials=BAhJIgGNOThmZGZhODExYTBhZTFlMjM1YzExZTNhNzNhMTZjYWE4OWNkYzRlNDlmNzRhOTEyYjgwYTc1MDQ1NTk3ZGViNDY4YWY0MjJkMmQ1NTMyOTlmMjg5NjQ1ZWE1ZDI1NWQzZTVjMTRmZWMzMTk3ZGQ0ZjUxNzAxZjlkMDEzZjkzYzE6OjUwMDAyMTQ1MDg4BjoGRVQ%3D--1748b28dcfb1aa77fcf6a152cd81f705e37328d5; _x_w=2000; _itildesk_session=VmpLaHpXSE1nVXVkaVE4aC9IMDhMc2ZlWmN5TWUwM1k5UzMvUU1uaEUwUE43N3laZTRkOG5rVEIxNUlGNjRYQTZubGFCazA5aGZTOUlteTZzZ1BHMmZFTjB0UHI2NzlHSlhHeDNsUTRkQXhWMElZWGowTk9qVE9ORUtYZmZOTk0yWW44clVXcHF1K1RpU1FGWm51bjBmSFEySnRGdnFiRHlqaU5SVTVCdzNveVVxdHR1MXNOcTc5RWhwTGdXOHZJZWtnNml1YlN5NWVndS83a1JuaUNIUWc5U0ZMUEdoZnd5YklFT2FmbEtCa2lzeHZ0eTkxZ2tOZm8yRTJUNkp4UDk3aUd3VjJyU3hUaGV5TEY1SmpoTnFmK0s1a054bjJqQ2hra3g4dmR4Q2c1VElIdVo4eTVYNUZFek5ObFpsTTUvQUxJcSthT1N6c01VOFFwc21hV3RFN3RjWHIycEh0YUExUGhxalp6cWFmNGQ1MEpIdEJOdEhWaVM0RWNuS2tvMVY5MVBBdk1lQTNOd3hwZW9IR2Z3TVlKdjM5WGx5bWEzS2V5YklLdDVUZVlCa3RWemhTWElMZmJWa2RwQjBYbC0tdVpDRUZaRjJ3S05qNmZ1MWg4WExhQT09--1520544af190876f5dd398f632a1e08dddb440cb' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data-binary $'-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n\u2713\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="authenticity_token"\r\n\r\njo/HKhd3sBSvy9jpeuee6O9dmuUAwdtOviEa8eUqD9qxh8tY+2IPTVNldZdjKMu1UEFjvrSRFbd12adgrti4Fw==\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="helpdesk_ticket[email]"\r\n\r\nmalla2020@student.hult.edu\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="cc_emails"\r\n\r\n\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="helpdesk_ticket[subject]"\r\n\r\n"""+ header + """\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="helpdesk_ticket[ticket_body_attributes][description_html]"\r\n\r\n<p>&nbsp;""" + body + """\041<br></p>\r\n\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][support_group_266987]"\r\n\r\nHult/Ashridge Technology\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="helpdesk_ticket[cmdb_requests_attributes][item_ids]"\r\n\r\n\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="meta[user_agent]"\r\n\r\nMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="meta[referrer]"\r\n\r\nhttps://ef-hult.freshservice.com/support/home\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="redactor_image_field"\r\n\r\n[]\r\n-----------------------------69017500537167808881873478305\r\nContent-Disposition: form-data; name="commit"\r\n\r\nSubmit\r\n-----------------------------69017500537167808881873478305--\r\n'"""

def solveTicket(id):
    os.system("""
    curl 'https://ef-hult.freshservice.com/helpdesk/tickets/""" + id + """/conversations/send_and_set_as' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="94"' \
  -H 'X-CSRF-Token: QUR17kVihmKPzQ1BasrypoK6q9AGwxzUIzVXpsFUdAPNa/WTTdsVytcjCDBzpR+mZrWH+8XROgcPauwhpbJ03Q==' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryncjb8nBoxgNcaLJc' \
  -H 'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Origin: https://ef-hult.freshservice.com' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://ef-hult.freshservice.com/helpdesk/tickets/292934' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Cookie: _BEAMER_USER_ID_bxOQALFw21023=cf2ad94d-7845-4e77-bebe-e31face3a383; _BEAMER_FIRST_VISIT_bxOQALFw21023=2021-09-08T09:00:32.723Z; _hp2_props.1080212440=%7B%22account_id%22%3A266987%2C%22account_state%22%3A%22active%22%2C%22account_plan%22%3A%22Enterprise%22%2C%22screenSize%22%3A%221920x1080%22%2C%22screenResolution%22%3A%221920x1080%22%7D; ajs_group_id=null; ajs_user_id=%2250003047319%22; ajs_anonymous_id=%2260a02599-e209-4c23-90f2-430babe983ce%22; ticket-filter-closed=false; _x_m=x_n; _x_w=2000; helpdesk_node_session=f51e74452371b00b11a6d6e78d28ff67b2bb0f58af09038b6dcf6f4f9927885664706dd00a81ee47eab4c7632a9b377806fadc1de204ef4d2ac7cd8bf42beda3; user_credentials=BAhJIgGNZGRhOWQxYTYyMjYyZGY4NzQwZDM0NTdkOTZkNGY2Zjk2ZTkxZjI2YWRkMDI1ZGEyMzgxMjc1YmJiZTVlNGZiMjlhMzFlMWJhMDIwOTdmMGYyMDNjNDY2NjU4YzZmZWVhOGIzNmVmMGY3MjkxZGE2NTMyZjg2ZmVhYjc4ZDVmYmU6OjUwMDAzMDQ3MzE5BjoGRVQ%3D--c86cef16486a72cd8eac30fad0b25c02b7f81155; filter_name=new_and_my_open; wf_order=created_at; wf_order_type=desc; _BEAMER_FILTER_BY_URL_bxOQALFw21023=true; _hp2_ses_props.1080212440=%7B%22r%22%3A%22https%3A%2F%2Flogin.microsoftonline.com%2F%22%2C%22ts%22%3A1634238509285%2C%22d%22%3A%22ef-hult.freshservice.com%22%2C%22h%22%3A%22%2Fhelpdesk%2Ftickets%22%7D; _BEAMER_LAST_POST_SHOWN_bxOQALFw21023=18977257; _BEAMER_BOOSTED_ANNOUNCEMENT_DATE_bxOQALFw21023=2021-10-14T19:10:59.426Z; _hp2_id.1080212440=%7B%22userId%22%3A%222062152184427793%22%2C%22pageviewId%22%3A%22773372359982846%22%2C%22sessionId%22%3A%22980754048603109%22%2C%22identity%22%3A%2250003047319%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _itildesk_session=SGZyNmdRU3RqWGxhYlYzdzJlMStPYnVuYWlZWWkyS0RIc3Azbnc0Wlluc1J0TkNhZWhHTFIxZlMrdzZpcFA5OFBrYlNMQ2l3ZnM0TWFRbTdPZ0NmK3NLajRwTERJRElWYVFQZ3FvdHFBUmJIc2ljSUFKbmc2UGM1eGN6TWJnUG9aRVdDN3FKa2d6TkMrZTQzVTF4R1gzL2luQmgvckJ0Tkpha0ptYU1STGdNaEkvVkxENnAwd0pTNlZzWE5GbmNOejA3UStZbGVKRGlLR3ZNanVKUndLakQ2c3g1VjVKSXZmL3ppS2Vrb0JCYlJIem5Mc0t5YXJMaTY5WWo5VDdUTFVmRjRvRmJEc0s2Q1RmaksxUGgvUXluTGd1aUFBQ2dFNFE1MXB1YTdBeFhYeldScG1XSCsrYUdLWFh1S1hBWFFBVi9CWUtEY0UxM2tWS0VXdXQ0QjFvZUUyUldYV1B6STY1SG1FNEg3a041RUdocjg0MUh5MlkxcFhXVXlhallFM2QrSUtFZ1dJOXFWMEx6VnRsNklDejkrT3piZHZwTGtKdW83OEVvQ3UvZXdEWkp1VHhRT1gvZDZLYlhDZ0NRcS0tZ2pHWTJ6cHUwL1lOd3hQaEtRN3dZQT09--889277be77fa385a1f7ce4700b79c07fbd5d52b2' \
  --data-raw $'------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n✓\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="authenticity_token"\r\n\r\nQUR17kVihmKPzQ1BasrypoK6q9AGwxzUIzVXpsFUdAPNa/WTTdsVytcjCDBzpR+mZrWH+8XROgcPauwhpbJ03Q==\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="reply_email[id]"\r\n\r\n"Tech Support" <tech.support@hult.edu>\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[note_body_attributes][body_html]"\r\n\r\n<div style="font-size: 14px; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, sans-serif;"><p></p><div><p>Ticket Resolved\u0021</p><p><br></p><p><br></p>\r\n<br><p><br></p>\r\n</div>\r\n</div>\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[note_body_attributes][full_text_html]"\r\n\r\n<div style="font-size: 14px; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Arial, sans-serif;"><p></p><div><p>Hi&nbsp;Mario,<br>Checks were done\u0021</p><p><br></p><p><br></p>\r\n<br><p><br></p>\r\n</div>\r\n</div><div class="freshdesk_quote">\r\n        <blockquote class="freshdesk_quote">On Thu, 14 Oct at  8:13 PM\r\n          <span class="separator"></span>,  Mario &lt;malla2020@student.hult.edu&gt;  wrote:\r\n          <div>&nbsp;The night Ceck and projectors shut down for class 3Bwas made\u0021<br>\r\n</div>\r\n\r\n        </blockquote>\r\n       </div>\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="quoted_text_html"\r\n\r\n<div class="freshdesk_quote">\r\n        <blockquote class="freshdesk_quote">On Thu, 14 Oct at  8:13 PM\r\n          <span class="separator" />,  Mario &lt;malla2020@student.hult.edu&gt;  wrote:\r\n          <div> The night Ceck and projectors shut down for class 3Bwas made\u0021<br>\r\n</div>\r\n\r\n        </blockquote>\r\n       </div>\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[bcc_emails]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[private]"\r\n\r\nfalse\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[source]"\r\n\r\n0\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[to_emails]"\r\n\r\nmalla2020@student.hult.edu\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[from_email]"\r\n\r\n"Tech Support" <tech.support@hult.edu>\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_note[email_config_id]"\r\n\r\n50000005444\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="add_notes_to_related_tickets[value]"\r\n\r\n0\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="redactor_image_field"\r\n\r\n"[]"\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="format"\r\n\r\njs\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="showing"\r\n\r\nnotes\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="utf8"\r\n\r\n✓\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="authenticity_token"\r\n\r\nC4/HEN6a+VsznFFHgu/VtD6cIq1DDOcwQlevjqA4evqHoEdt1iNq82tyVDabgDi02pMOhoAeweNuCBQJxN56JA==\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[priority]"\r\n\r\n1\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[status]"\r\n\r\n4\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[source]"\r\n\r\n2\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[ticket_type]"\r\n\r\nIncident\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[urgency]"\r\n\r\n1\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[impact]"\r\n\r\n1\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[group_id]"\r\n\r\n50000059932\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[responder_id]"\r\n\r\n50003047319\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[department_id]"\r\n\r\n50000268963\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[category]"\r\n\r\nOperation\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[sub_category]"\r\n\r\nMaintenance Checks\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[item_category]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][location_266987]"\r\n\r\nLondon &gt; UG Campus\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][country_266987]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][service_team_266987]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][ticket_type_266987]"\r\n\r\nRequest\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][enrolment_status_266987]"\r\n\r\nHult Student\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][enrolment_status_student_266987]"\r\n\r\nMatriculated\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][i_confirm_this_case_has_been_fully_delivered_as_per_the_request_266987]"\r\n\r\n0\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][support_group_266987]"\r\n\r\nHult/Ashridge Technology\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][transfer_ticket_266987]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk_ticket[custom_field][group_266987]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="helpdesk[tags]"\r\n\r\n\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="send_and_set"\r\n\r\ntrue\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="send_and_set_for_br"\r\n\r\n4\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc\r\nContent-Disposition: form-data; name="actual_action"\r\n\r\nreply\r\n------WebKitFormBoundaryncjb8nBoxgNcaLJc--\r\n' \
  --compressed
    """)

def createAndSolveTicket(header, body):
    command = os.popen(createTicket(header, body)).read()
    id = command.split('href="https://ef-hult.freshservice.com/support/tickets/')[1].split('"')[0]
    print(command)
    print('Solving ticket with id: ' + id)
    solveTicket(f'{id}')

def doNightChecks():
    classes = ['LGA', 'LGB', 'GA', 'GB', '1A', '1B', '2A', '2B', '3A', '3B']
    ids = []
    for clas in classes: 
        command = os.popen(createTicket(header='Doing Night Check for Class ' + clas, 
                    body='The night check for Class: ' + clas + ' did not result in any issues. This class is now shut down and ready for the next day!')).read()
        id = command.split('href="https://ef-hult.freshservice.com/support/tickets/')[1].split('"')[0]
        print(command)
        print('Solving ticket with id: ' + id)
        ids.append(id)
    for id in ids:
        solveTicket(id)

def doMorningChecks():
    classes = ['LGA', 'LGB', 'GA', 'GB', '1A', '1B', '2A', '2B', '3A', '3B']
    classes = ['LGA', 'LGB', 'GA', 'GB', '1A', '1B', '2A', '2B', '3A', '3B']
    ids = []
    for clas in classes: 
        command = os.popen(createTicket(header='Setting up class ' + clas + ' for class today', 
                    body=clas + ' Was sucessfully set up without any issues, and it ready for class today')).read()
        id = command.split('href="https://ef-hult.freshservice.com/support/tickets/')[1].split('"')[0]
        print(command)
        print('Solving ticket with id: ' + id)
        ids.append(id)
    for id in ids:
        solveTicket(id)


# main.py
import sys

if __name__ == "__main__":
    if (sys.argv[1] == 'morning'):
        print(f"doing morning check: {len(sys.argv)}")
        doMorningChecks()
    elif (sys.argv[1] == 'night'):
        doNightChecks()
        print(f"doing night check: {len(sys.argv)}")
    else:
        print(""" 
        _______ HOW TO USE ______
        Do morning checks, type command: python3 main.py morning
        Do night checks, type command: python3 main.py night
        """)


# doMorningChecks()


# doNightChecks()

#                       Title                            Description
# createAndSolveTicket('Reset & Update Software in 1B', 'Updating the mac mini in the 1B class')


# solveTicket('294336')



# x = requests.post("https://portal.ezeep.com/p1/documents/upload", {
#     "credentials": "include",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "Accept-Language": "en-GB,en;q=0.5",
#         "X-Requested-With": "XMLHttpRequest",
#         "Content-Type": "multipart/form-data; boundary=---------------------------66437898040123963133230447290",
#         "Sec-Fetch-Dest": "empty",
#         "Sec-Fetch-Mode": "cors",
#         "Sec-Fetch-Site": "same-origin",
#         "Pragma": "no-cache",
#         "Cache-Control": "no-cache"
#     },
#     "referrer": "https://portal.ezeep.com/",
#     "body": "",
#     "method": "POST",
#     "mode": "cors"
# })

# print ( x.status_code, x.json)
