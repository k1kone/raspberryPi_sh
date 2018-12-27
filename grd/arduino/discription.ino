/*
●void cmd(String c)
●
●
●
●


★★コマンド ★★
【 void cmd(String c) 】
シリアルポートの文字を判定し、各コマンドを実行します。

　c == "s" :[sound on]アラーム音を1度鳴らします。
            ※almMelody()を一度実行
            
  c == "c" :[clear settin] LEDを消灯、各フラグを初期化します。
            ※各フラグに0を代入、lightOff(void)を一度実行。
            
  c == "a" :[alert] 設定時間超過の警告としてalert_flgが立っている間、LEDを赤色点滅させます 。
            remind_flgに0を代入することで、リマインド(LED青色点滅)を停止、
            remind_flgに1を代入することで、アラート(LED青色点滅)を開始。
  
  c == "r" :[remind] 設定時間前にリマインドとしてalert_flgが立っている間、LEDを青色点滅させます 。
            remind_flgに1を代入することで、リマインド(LED青色点滅)を開始、
            fnc_flgに1を代入することで、ボタン判定関数 checkButton() を呼び出します。

  c == "b" :[] タイマー、メールアドレス未設定時のスタンバイ状態を解除します。
              stanby_flgをfalseにする

  c == "v" :[] スタンバイ状態にします。
              stanby_flgをtrueにする

  c == "d" :[display DHT] DHTから温度・湿度を読み取り、シリアルポートへ出力しラズベリーパイに渡す。


------------------------------------------------------------------
      




 
 */
