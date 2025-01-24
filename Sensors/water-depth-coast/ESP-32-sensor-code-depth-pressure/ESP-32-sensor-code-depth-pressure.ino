#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>

// Définir le pin analogique pour le capteur MaxSonar
#define PIN_ANALOG A8 // Ajustez si nécessaire
#define VOLTAGE_REF 3.3 // Tension de référence de l'ESP32
#define CM_PER_VOLT 102 // Facteur pour convertir la tension en distance (en cm)
#define SCALE_FACTOR 1024.0 // Résolution ADC (10 bits)

// Constante pour la pression au niveau de la mer (hPa)
#define SEA_LEVEL_PRESSURE 1015.0

// Objet BME680
Adafruit_BME680 bme;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // Initialisation du capteur BME680
  if (!bme.begin(0x77)) { // Adresse I2C par défaut
    Serial.println("Erreur: BME680 introuvable !");
    while (1);
  }

  // Configurer les paramètres de mesure pour le BME680
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // Température du chauffe-gaz à 320°C pendant 150 ms

  // Configurer la résolution de l'ADC pour le capteur analogique
  analogReadResolution(12); // Résolution de 12 bits pour l'ESP32
}

void loop() {
  // Lecture du BME680
  if (bme.performReading()) {
    float temperature = bme.temperature;
    float pressure = bme.pressure / 100.0; // Convertir en hPa
    float altitude = bme.readAltitude(SEA_LEVEL_PRESSURE);

    // Afficher les données du BME680
    Serial.println("=== Données du BME680 ===");
    Serial.print("Température: ");
    Serial.print(temperature);
    Serial.println(" °C");

    Serial.print("Pression: ");
    Serial.print(pressure);
    Serial.println(" hPa");

    Serial.print("Altitude estimée: ");
    Serial.print(altitude);
    Serial.println(" m");
  } else {
    Serial.println("Erreur de lecture du BME680 !");
  }

  // Lecture du capteur MaxSonar
  int rawValue = analogRead(PIN_ANALOG);
  float voltage = (rawValue / SCALE_FACTOR) * VOLTAGE_REF;
  float distance = voltage * CM_PER_VOLT;

  // Afficher les données du MaxSonar
  Serial.println("=== Données du MaxSonar ===");
  Serial.print("Valeur brute ADC: ");
  Serial.println(rawValue);

  Serial.print("Tension lue (V): ");
  Serial.println(voltage, 3);

  Serial.print("Distance mesurée (cm): ");
  Serial.println(distance);

  // Pause entre les lectures
  Serial.println("============================\n");
  delay(2000);
}
