#include <LWiFi.h>
#include <DHT.h>
#include <Wire.h>
#include "SI114X.h"
DHT dht11_p2(2, DHT11);
SI114X SI1145 = SI114X();


char ssid[] = "your_wifi_name";      //  your network SSID (name)
char pass[] = "your_wifi_password";      // your network password
int keyIndex = 0;              

int status = WL_IDLE_STATUS;
char server[] = "server IP";  // 輸入ip

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
WiFiClient client;

void setup() {
    // dht11_p2.begin();

    // Initialize serial and wait for port to open:
    Serial.begin(9600);

     while (!SI1145.Begin()) {
      delay(1000);
    }
    
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }

    // attempt to connect to Wifi network:
    while (status != WL_CONNECTED) {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
        status = WiFi.begin(ssid, pass);
    }
    Serial.println("Connected to wifi");
    printWifiStatus();

    Serial.println("\nStarting connection to server...");
    // if you get a connection, report back via serial:
}

void loop() {
    // if there are incoming bytes available
    // from the server, read them and print them:

    if (client.connect(server, 8000)) {
        String PostData = buildJson();  
        Serial.println("connected to server (GET)");
        // Make a HTTP request:
        client.println("POST /api/POST_IoT_sensor_info HTTP/1.1");

        client.println("Host: 192.168.43.225:8000");        // 更改ip
        client.println("Authorization: Basic cm9vdDpyb290"); // 更改Authorization
        client.println("Connection: close");

        // set Content Type to json object
        client.println("Content-Type: application/json");

        // set Content Length
        client.print("Content-Length: ");
        client.println(PostData.length());
        client.println();
        
        // send the HTTP POST body
        client.println(PostData);
        client.println();       
        Serial.println(PostData);
        // delay(1000);
        
        
    }
    
    while (client.available()) {
        char c = client.read();
        Serial.write(c);
    }

    // if the server's disconnected, stop the client:
    if (!client.connected()) {
        Serial.println();
        Serial.println("disconnecting from server.");
        client.stop();

        // do nothing forevermore:
        while (true);
    }

   
}



// create JSON file
String buildJson() {
  delay(10000); //暫設10秒
  float temp =dht11_p2.readTemperature(); // 溫度
  float humi =dht11_p2.readHumidity(); // 濕度
  int moisturePin = A0; // 土壤感測器插槽位置
  int moisture = 0; // 土壤感測器起始值
  moisture = analogRead(moisturePin); // 土壤
  int light = SI1145.ReadIR(); // IR
  float UV =(float)SI1145.ReadUV()/100; // sunlight
  
  String data = "{";
  data+="\"temp\": ";
  data+=temp;
  data+=",";
  data+="\"humi\": ";
  data+=humi;
  data+=",";
  data+="\"light\": ";
  data+=light;
  data+=",";
  data+="\"UV\": ";
  data+=UV;
  data+=",";
  data+="\"moisture\": ";
  data+=moisture;
  data+="}";
  return data;
}

void printWifiStatus() {
    // print the SSID of the network you're attached to:
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());

    // print your WiFi shield's IP address:
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);

    // print the received signal strength:
    long rssi = WiFi.RSSI();
    Serial.print("signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
}