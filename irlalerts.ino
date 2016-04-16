int boardLed = D7;

void setup() {
        pinMode(boardLed, OUTPUT);
        Particle.subscribe("donation", donationAlert);
        Particle.subscribe("subscription", subscriptionAlert);
}

void donationAlert(const char *event, const char *data)
{
        Spark.publish("fromDevice", "donation received");
        digitalWrite(boardLed,HIGH);
}

void subscriptionAlert(const char *event, const char *data)
{
        Spark.publish("fromDevice", "subscription received");
        digitalWrite(boardLed,LOW);
}
