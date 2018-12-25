<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>test</title>
</head>
<body>

    <header><div class="wrap"><a class="log" href="/"><img src="https://raw.githubusercontent.com/k1kone/raspberryPi_sh/master/grd/img/logo_424242.png" ></a>
    <nav>
        <ul>
            %for i, j in navlis.items():
                <li><a href="{{j}}">{{i}}</a></li>
            %end
        </ul>
    </nav></div>
    </header>
    <article>
		<div class="flex">
        <section>
            <h2 id="measure">温度・湿度測定</h2>
			<div class="dht">
				<div id="dht_t" class="normal"><p>温度<span class="num">{{dht_t}}</span><span class="kigo">℃</span></p></div>
				<p id="modtxt1" class="normal">{{modtxt1}}</p>
				<div id="dht_h" class="normal"><p>湿度<span class="num">{{dht_h}}</span><span class="kigo">%</span></p></div>
				<p id="modtxt1" class="normal">{{modtxt2}}</p>
			</div>
			<p class="mod">{{mod}}</p>

            
        </section>
        <section>
            <h2>アラーム</h2>
			
            %for ind,i in enumerate(almls):
				<div class="timetable"><p><span class="num">{{ind}}</span>{{i['h']}}:{{i['m']}}</p></div>
            %end
			
            <p>{{stat}}</p>
        </section>
		</div>
		<section class="roadara flex">
			<p>データ更新｜{{ntime}}</p><p id="rlbtn">リロード</p>
		</section>
    </article>


<script>
    window.onload = function(){
            setTimeout('location.reload()', 10000);
		
            let btn = document.getElementById('rlbtn');
            btn.addEventListener('click', function(){ location.reload()});
    };
</script>
</body>
</html>
<!--
dht=dht
navlis = navlis,
ntime=nowtime.now().strftime('%Y, %m, %d, %H:%M:%S'), 
mod=mod 
modtxt=modtxt
-->
