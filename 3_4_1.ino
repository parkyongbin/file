#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  float di = discomfortIndex();
  if(di != 0)
  {
    Serial.print("불쾌지수: ");
    Serial.println(di);
  }
}

int discomfortIndex()
{
  static unsigned long currTime = 0;
  static unsigned long prevTime = 0;

  currTime = millis();
  if (currTime - prevTime >= 2000)
  {
    prevTime = currTime;
    float humi = dht.readHumidity();
    float temp = dht.readTemperature();

    if (!isnan(humi) || !isnan(temp))
    {
      float di = (1.8 * temp) - (0.55 * (1 - humi / 100.0) * (1.8 * temp - 26)) + 32;
      return di;
    }
  }

  return 0;
}
