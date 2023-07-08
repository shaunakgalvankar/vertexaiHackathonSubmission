# import streamlit as st
# from azure.identity import DefaultAzureCredential
# from azure.media.services.aio import AzureMediaServices
# from azure.media.streaming.aio import StreamingEndpoint

# # Authenticate with Azure
# credential = DefaultAzureCredential()
# ams_client = AzureMediaServices(credential)

# # Create a streaming endpoint
# endpoint_name = "my-streaming-endpoint"
# endpoint_location = "westus"
# streaming_endpoint = await ams_client.streaming_endpoints.create_or_update(
#     resource_group_name="<your-resource-group-name>",
#     account_name="<your-azure-media-services-account-name>",
#     streaming_endpoint_name=endpoint_name,
#     parameters=StreamingEndpoint(
#         location=endpoint_location,
#         ...  # Add any other necessary parameters
#     ),
# )

# # Start the streaming endpoint
# await streaming_endpoint.start()

# # Display the streaming endpoint information
# st.write(f"Streaming Endpoint Name: {streaming_endpoint.name}")
# st.write(f"Streaming Endpoint URL: {streaming_endpoint.host_name}")