def mpesa_callback_data_distructure(data):
    try:
        callback_data = data['Body']['stkCallback']
        callback_object = {
            "MerchantRequestID": callback_data.get("MerchantRequestID"),
            "CheckoutRequestID": callback_data.get("CheckoutRequestID"),
            "ResultCode": callback_data.get("ResultCode"),
            "ResultDesc": callback_data.get("ResultDesc"),
            "Amount": [x["Value"] for x in callback_data["CallbackMetadata"]["Item"] if x['Name'] == "Amount"][0],
            "TransactionTimeStamp":  [x["Value"] for x in callback_data["CallbackMetadata"]["Item"] if x['Name'] == "TransactionDate"][0],
            "PhoneNumber":  [x["Value"] for x in callback_data["CallbackMetadata"]["Item"] if x['Name'] == "PhoneNumber"][0],
            "MpesaReceiptNumber":  [x["Value"] for x in callback_data["CallbackMetadata"]["Item"] if x['Name'] == "MpesaReceiptNumber"][0],
        }
        return callback_object
    except Exception as e:
        raise e
