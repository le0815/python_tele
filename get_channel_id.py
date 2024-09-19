from telethon.sync import TelegramClient

api_id = 24259180
api_hash = "63cf9778009838a7d48f75866a5b6fc9"
phone_number = '+84559762813'

client = TelegramClient('khanh_chi', api_id, api_hash)

async def get_channel_id(channel_username):
    await client.start(phone_number)

    try:
        # Get the entity (channel) by username
        channel_entity = await client.get_entity(channel_username)

        # Print the channel ID
        print(f"Channel ID for {channel_username}: {channel_entity.id}")

    except Exception as e:
        print(f"Error getting channel ID: {e}")

if __name__ == '__main__':
    channel_username = 'https://t.me/sdfsdfsq'
    client.loop.run_until_complete(get_channel_id(channel_username))