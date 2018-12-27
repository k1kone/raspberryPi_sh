#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11

#define ButtonPin 3
int buttonState = 0;

float h;
float t;

#define RedPin 11
#define BluePin 10
#define GreenPin 9
int r, g, b;

//flag setting
bool setup_flg = false;
bool stanby_flg = false;
bool fanc_flg = false;
bool remind_flg = false;
bool alert_flg = false;

String judge ="=\n";

 
DHT dht(DHTPIN, DHTTYPE); 
String msgRead;

void setup() {
    Serial.begin(9600);
    dht.begin();

    //button setup
    pinMode(ButtonPin, INPUT_PULLUP);

    //LED setup
    pinMode(RedPin, OUTPUT);
    pinMode(BluePin, OUTPUT);
    pinMode(GreenPin, OUTPUT);
    r = 0;
    g = 0;
    b = 0;
}
 
void loop() {
  setupcmp();
  h = dht.readHumidity();
  t = dht.readTemperature();
  inpSrial();
  
  if(stanby_flg){
    //lightOff();
    analogWrite(RedPin, 255);
    analogWrite(BluePin, 255);
    analogWrite(RedPin, 255);
  }
  
  if(remind_flg && !alert_flg){
    flash_loop(BluePin, remind_flg);
  }else if(!remind_flg && alert_flg){
    flash_loop(RedPin, alert_flg);
  }
  if(fanc_flg){
    //judge = "_\n";
    checkButton();
  }else{judge = "waiting\n";}
}// loop end

//// シリアルポート入力 ////
 //input siriarlport word 
 void inpSrial(void){
    if(Serial.available() > 0) {
      msgRead = Serial.readStringUntil('\n'); // '\n'まで文字列を読み込む
      cmd(msgRead);
    } 
    msgRead = "";
 }


//// シリアルポート出力 ////

void dhtdisp(float h, float t){
    String date = "{'H':" + String(h) + ", 'T':" + String(t)+"}\n";
    Serial.print(date);
}

void setupcmp(void){
  if(!setup_flg){
    String date = "setupcmp";
    Serial.println(date);
    setup_flg = true;
  }
}

//// コマンド ////
void cmd(String c){
    if(c == "s"){
      //sound on
      almMelody();
      
    }else if(c == "c"){
      //clear setting
      fanc_flg= false;
      alert_flg = false;
      remind_flg = false;
      //judge = "=\n";
      lightOff();
      
    }else if(c == "a"){
      //alert"
      alert_flg = true;
      fanc_flg= true;
      remind_flg = false;
    
    }else if(c == "r"){
      //rimind
      alert_flg = false;
      remind_flg = true;
      fanc_flg= true;
      
     }else if(c == "b"){
      stanby_flg = false;
      alert_flg = false;
      remind_flg = false;
      /*delay(500);
      lightOff();
      delay(500);
      flash_LED(GreenPin, 3, 200);*/
      
     }else if(c == "v"){
      stanby_flg = true;
      alert_flg = false;
      remind_flg = false;
      fanc_flg= false;
      
     }else if(c == "d"){
      //display DHT on sirial port
      dhtdisp(h, t);
    }else if(c=="j"){
       Serial.print(judge);
    }
}

//// ボタン判定 ////
 //check button 
 void checkButton(void){

    buttonState = digitalRead(ButtonPin);
    if(buttonState == LOW){
      if(remind_flg || alert_flg){
        judge = "o\n";
      }else{
        judge = "x\n";
      }
      
      flash_LED(GreenPin, 3, 700);
      lightOff();
      remind_flg = false;
      alert_flg = false;
    }
 }

//// LED関連関数 ////

void flash_LED(int rgb, int x, int times){
  //int pin = rgb;
  int r =x;
  if(r<1)r = 3;
  while(r>0){
    delay(times);
    analogWrite(rgb, 100);
    delay(times);
    analogWrite(rgb, 0);
    r--;
  }
  lightOff();
}

void flash_loop(int rgb, bool flg){
  lightOff();
  if(flg){
    analogWrite(rgb, 100);
    delay(700);
    analogWrite(rgb, 0);
    delay(700);
  }
}

void lightOff(void){
  analogWrite(RedPin, 0);
  analogWrite(BluePin, 0);
  analogWrite(RedPin, 0);
}
