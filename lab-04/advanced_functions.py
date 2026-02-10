"""
Advanced Functions Module
Contains functions to be tested with property-based testing and mocking.
"""

import requests

def reverse_string(text):
    """
    Reverse a string.

    Args:
    text (str): Input string

    Returns:
    str: Reversed string

    Examples:
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    """
    return text[::-1]

def process_user_login(user_id, database, notification_service):
    """
    Process user login: fetch user data and send notification.

    Args:
    user_id (int): User ID
    database: Database connection object with get_user() method
    notification_service: Notification service object with send_email() method

    Returns:
    dict: User data dictionary if user exists, None otherwise

    Examples:
    >>> # Mock database and notification service would be used in tests
    >>> # user = process_user_login(1, mock_db, mock_notification)
    """
    user = database.get_user(user_id)
    if user:
        notification_service.send_email(user['email'], 'Login successful')
        return user
    return None

def get_weather_report(city):
    """

    Fetch weather data from external API.

    Args:
    city (str): City name

    Returns:
    dict: Weather data dictionary or error message

    Examples:
    >>> # In tests, requests.get will be mocked
    >>> # weather = get_weather_report('Bangkok')
    """
    try:
        response = requests.get(f'https://api.weather.com/data/{city}')
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'City not found'}
    except Exception as e:
        return {'error': str(e)}