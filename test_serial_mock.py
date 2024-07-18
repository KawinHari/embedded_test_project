import pytest
from unittest.mock import patch, MagicMock

# Test case for validating a command response with mock
def test_command_response():
    def send_command(command):
        with patch('serial.Serial') as mock_serial:
            mock_serial_instance = MagicMock()
            mock_serial.return_value = mock_serial_instance
            mock_serial_instance.readline.return_value = b"OK"
            
            ser = serial.Serial('/dev/ttyUSB0', 9600)
            ser.write(command.encode())
            response = ser.readline().decode()
            ser.close()
            return response

    command = "TEST"
    expected_response = "OK"
    assert send_command(command) == expected_response
