import pieces_os_client
import platform
import tkinter.messagebox as messagebox
# Defining the port based on the operating system. For Linux, the port is 5323, and for macOS/Windows, the port is 1000.
platform_info = platform.platform()
if 'Linux' in platform_info:
    port = 5323
else:
    port = 1000

# The `basePath` defaults to http://localhost:1000, however we need to change it to the correct port based on the operating system.
configuration = pieces_os_client.Configuration(host=f"http://localhost:{port}")

# Initialize the Pieces ApiClient
api_client = pieces_os_client.ApiClient(configuration)

# Enter a context with an instance of the ApiClient
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the WellKnownApi class
    api_instance = pieces_os_client.WellKnownApi(api_client)

    try:
        # Retrieve the (wellknown) health of the Pieces OS
        api_response = api_instance.get_well_known_health()
        print("The response of WellKnownApi().get_well_known_health:")
        print(api_response) # Response: ok
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_health: %s\n" % e)

print("Hello World")
def Question():
    #Display a response Type to a Question
    response=messagebox.askquestion("Hello Which sport you want to play today Hockey or Football")

    if response=="yes":
        print("The User wants to play Hockey")
    elif response=="no":
        print("The User wants to play Football")
    else:
        print("The User is not interested in either Hockey or Football")
Question()
    