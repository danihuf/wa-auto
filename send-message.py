import pywhatkit as waKit
import csv
import time

def load_csv_data(file_path):
    data_dict = {}
    
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the header row if it contains column names
        next(csv_reader, None)
        
        for row in csv_reader:
            name, phone_number = row
            data_dict[name] = phone_number
    
    return data_dict

def send_whatsapp_messages(data_dict, message_template):
    for name, phone_number in data_dict.items():
        try: 
            formatted_message = message_template.format(name)
            # send message with delay before closing tab
            waKit.sendwhatmsg_instantly(phone_number, formatted_message, 10, True, tabCloseDelay)
            print(f"Message sent to {name} at {phone_number}: {formatted_message}")
            time.sleep(waitTimeBetweenMessages)

            # # Wait and periodically check for the sent message
            # message_sent = False
            # max_check_attempts = 5  # Adjust as needed
            # check_interval = 10  # Seconds, adjust as needed
            # message_sent = False

            # for _ in range(max_check_attempts):

            #     if waKit.sendwhatmsg_instantly(phone_number, formatted_message, 10, True, 25):
            #         message_sent = True
            #         break
            #     time.sleep(check_interval)
            
            # if message_sent:
            #     print(f"Message sent to {name} at {phone_number}: {formatted_message}")
            # else:
            #     print(f"Failed to send message to {name} at {phone_number}")

        except waKit.CallTimeException as e:
            print(f"Error sending message to {name} at {phone_number}: {e}")

# Define path to csv file with contacts
# csv should be structured as: name,phone
csvPath = './contacts.csv'
data_dict = load_csv_data(csvPath)
# Define how long script waits to close tab after sending message, increase if internet connection is slow
tabCloseDelay = 30
# Define how long script waits to open a new tab in between contacts
waitTimeBetweenMessages = 30
# Define your message template
message_template = "Hello, {}! This is a automated message for testing purposes."
# send messages to all contacts in csv
send_whatsapp_messages(data_dict, message_template)

