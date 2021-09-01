url = "https://esigngenie.com/esign/api/templates/createFolder"
# frappe.response["args"]=(frappe.form_dict)
# company = frappe.response["args"]["company"]
request_data = frappe.form_dict
company = request_data.company

frappe.log_error(company)
payload = ({
  "folderName": "Test Document",
  "templateIds": [
    201963
  ],
  "fields": {
    "company": company
  },
  "parties": [
    {
      "firstName": "Anushka",
      "lastName": "Trivedi",
      "emailId": "anushka@onehash.ai",
      "permission": "FILL_FIELDS_AND_SIGN",
      "sequence": 1
    }
  ],
  "fixRecipientParties": True,
  "fixDocuments": True,
  "hideAddNewButton": True,
  "createEmbeddedSigningSession": True,
  "createEmbeddedSigningSessionForAllParties": True,
  "sessionExpire": True,
  "expiry": 600000
})
headers = {
  'Authorization': 'Bearer 1c4772e5bcee466ebbbf1a22c91fdaf7',
  'Content-Type': 'application/json',
  'Cookie': 'AWSALB=A/kb+IDu6gr08bLgP2mnVJex9nYf7tfZKuRU+YGV1PNGsz7XrsZ5tKOk7n0iXehxvbVpZVslYtjiGq/GTuUP0I92HZI6MlqBv2EwMDrToXCbi0KXRX4WSYGuHjKM; AWSALBCORS=A/kb+IDu6gr08bLgP2mnVJex9nYf7tfZKuRU+YGV1PNGsz7XrsZ5tKOk7n0iXehxvbVpZVslYtjiGq/GTuUP0I92HZI6MlqBv2EwMDrToXCbi0KXRX4WSYGuHjKM'
}

response = frappe.make_post_request(url=url, headers=headers, data=json.dumps(payload))
frappe.response['message'] = response
