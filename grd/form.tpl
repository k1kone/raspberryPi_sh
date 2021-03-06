<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>setting</title>
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
        <section>
            <h2 id="alarm">アラーム</h2>
            %if not almls:
                <p class="noalm">アラームが設定されていません。</p>
            %else:
                %for ind,i in enumerate(almls):
                    <div class="timetable flex"><p><span class="num">{{ind+1}}</span>{{str(i['h']).zfill(2)}}:{{str(i['m']).zfill(2)}}</p><a href="/del/{{i['n']}}">削除</a></div>
                %end
            %end
			
			
        <form action="" method="POST">
            <input type="number" name="time_h" min="0" max="23" value="0" /> 時
            <input type="number" name="time_m" min="0" max="59" step="10" value="0" />分
            <input type="submit" value="登録"/>
        </form>
        </section>
		<section class="roadara flex">
			<p>{{ntime}}</p><!--p id="rlbtn">リロード</p-->
		</section>
    </article>
<style>
*{
	box-sizing:border-box;
	font-family: 游ゴシック体,Yu Gothic,YuGothic,\\30D2\30E9\30AE\30CE\89D2\30B4\30B7\30C3\30AF Pro,Hiragino Kaku Gothic Pro,Source Sans Pro,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,sans-serif;
}
body{
	padding:0;
	margin:0;
	/*background:url('http://www.netyasun.com/home/bk-img/b039.gif');*/
	background:#D4D4D4;
	background-size:10%;
	font-size:100%;
}
header{
	background:#fff;
	padding-bottom:1rem;
	margin-bottom:1rem;
}

header .wrap{
	display:flex;
	flex-flow: row wrap;
	justify-content:space-between;
	align-items:flex-end;
	/*max-width:960px;*/
	width:960px;
	margin:0 auto;
}

header a.log{
	display:block;
	height:6em;
}

header a.log img{
	width:auto;
	height:100%;
}

header nav ul{
	display:flex;
	flex-flow: row wrap;
	justify-content: flex-end;
	list-style:none;
	padding:0;
	margin:0;
}

header nav li{
	margin:0 0.5em 0.5em 0;
	font-size:1.5rem;
	padding-left:1.75rem;
    position:relative;
}
header nav li:first-child{
	margin-right:1.5rem;
}	
header nav li::before{
	content:'';
	width:1em;
	height:1em;
	background:url('https://raw.githubusercontent.com/k1kone/raspberryPi_sh/master/grd/img/home.png') no-repeat center left;
	background-size:contain;
	position:absolute;
	top:0.3em;
	left:0;
}
	
header nav li:last-child::before{
background:url('https://raw.githubusercontent.com/k1kone/raspberryPi_sh/master/grd/img/setting.png') no-repeat center left;
	background-size:contain;
}
header nav a{
	color:#424242;
	text-decoration:none;
}

article{
	margin:0 auto;
	/*max-width:960px;*/
	width:960px;
}

.flex{
	display:flex;
	flex-flow: row wrap;
	justify-content:space-between;
	/*justify-content: space-around;*/
	align-items:stretch;
}

section{
	flex: 1;
	margin:0.5rem;
	background:rgba(255,255,255,.9);
	padding:1rem;
	border-radius:3px;
	border:1px solid #C9C9C9;
	box-shadow:1px 1px 5px rgba(0,0,0,.2);
	font-size:1.25rem;
}

article h2{
	font-weight:normal;
	font-size:2.5rem;
	margin:0;
	color:#424242;
	padding-left:2.75rem;
	padding-bottom:0.25rem;
	border-bottom:solid 1px #C9C9C9;
	position:relative;
}

#measure::before{
	content:"";
	width:2.2rem;
	height:2.2rem;
	position:absolute;	background:url('https://raw.githubusercontent.com/k1kone/raspberryPi_sh/master/grd/img/grp.png') no-repeat center left;
	background-size:contain;
	top:0.7rem;
	left:0;
}
#alarm{
	margin-bottom:1rem;
}
#alarm::before{
	content:"";
	width:2.2rem;
	height:2.2rem;
	position:absolute;
	background:url('https://raw.githubusercontent.com/k1kone/raspberryPi_sh/master/grd/img/alm.png') no-repeat center left;
	background-size:contain;
	top:0.7rem;
	left:0.2rem;
}

#dht_t p,#dht_h p{
	font-size:1.5rem;
	vertical-align:bottom;
	padding:0;
	margin:0;
	overflow-y:hidden;
	height:10.5rem;
}

.dht p .num{
	font-size:8rem;
}

.dht p .kigo{
	font-size:4rem;
}

#modtxt1,#modtxt2{
	padding:0;
	margin:0 0 1.5em 1.25rem;
	font-size:1.5rem;
}

.mod{
	font-size:1.25rem;
	line-height:1.5em;
}

#dht_t p::before,#dht_h p::before{
    font-size:7.5rem;
	margin-right:0.5rem;
	vertical-align:bottom;
}

#modtxt1::before,#modtxt2::before{
    font-size:1.5rem;
	margin-right:0.5rem;
	vertical-align:center;
}


#dht_t.normal .num,#dht_t.normal .kigo,#dht_h.normal .num,#dht_h.normal .kigo,#modtxt1.normal,#modtxt2.normal{
	color:#00B81A;
}

#dht_t.normal p::before,#dht_h.normal p::before{
	content:"○";
	color:#00B81A;
}

#modtxt1.normal::before,#modtxt2.normal::before{
	content:"◎";
	color:#00B81A;
}

#dht_t.hard_u .num,#dht_t.hard_u .kigo,#dht_h.hard_u .num,#dht_h.hard_u .kigo,#modtxt1.hard_u,#modtxt2.hard_u{
	color:#E67C00;
}

#dht_t.hard_u p::before,#dht_h.hard_u p::before{
	content:"△";
	color:#E67C00;
}

#modtxt1.hard_u::before,#modtxt2.hard_u::before{
	content:"▲";
	color:#E67C00;
}


#dht_t.hard_d .num,#dht_t.hard_d .kigo,#dht_h.hard_d .num,#dht_h.hard_d .kigo,#modtxt1.hard_d,#modtxt2.hard_d{
	color:#12BDF5;
}

#dht_t.hard_d p::before,#dht_h.hard_d p::before{
	content:"△";
	color:#12BDF5;
}

#modtxt1.hard_d::before,#modtxt2.hard_d::before{
	content:"▲";
	color:#12BDF5;
}

#dht_t.hard_d .num,#dht_t.hard_d .kigo,#dht_h.hard_d .num,#dht_h.hard_d .kigo,#modtxt1.hard_d,#modtxt2.hard_d{
	color:#12BDF5;
}

#dht_t.hard_d p::before,#dht_h.hard_d p::before{
	content:"△";
	color:#12BDF5;
}

#modtxt1.hard_d::before,#modtxt2.hard_d::before{
	content:"▲";
	color:#12BDF5;
}

#dht_t.dng_d .num,#dht_t.dng_d .kigo,#dht_h.dng_d .num,#dht_h.dng_d .kigo,#modtxt1.dng_d,#modtxt2.dng_d{
	color:#235ACC;
}

#dht_t.dng_d p::before,#dht_h.dng_d p::before{
	content:"×";
	color:#235ACC;
}

#modtxt1.dng_d,#modtxt2.dng_d{
	font-weight:bold;
}

#modtxt1.dng_d::before,#modtxt2.dng_d::before{
	content:"!";
	font-weight:bold;
	color:#235ACC;
}

#dht_t.dng_u .num,#dht_t.dng_u .kigo,#dht_h.dng_u .num,#dht_h.dng_u .kigo,#modtxt1.dng_u,#modtxt2.dng_u{
	color:#ED3535;
}

#dht_t.dng_u p::before,#dht_h.dng_u p::before{
	content:"×";
	color:#ED3535;
}

#modtxt1.dng_u,#modtxt2.dng_u{
	font-weight:bold;
}

#modtxt1.dng_u::before,#modtxt2.dng_u::before{
	content:"!";
	font-weight:bold;
	color:#ED3535;
}

.timetable{
	width:95%;
	margin:0 auto;
	font-size:2rem;
	align-items:center;
}

.timetable p{
	margin:1rem 0;

}
.timetable .num{
	width:2rem;
	text-align:center;
	display:inline-block;
	padding:0.5rem;
	line-height:1em;
	background:#424242;
	color:#fff;
	border-radius:3px;
	border-collapse:collapse;
	margin-right:0.25em;
}

.timetable:not(:last-child){
	border-bottom:dotted 1px #C9C9C9;
	margin-bottom:0.5rem;
}

.timetable a{
    display:inline-block;
	text-decoration:none;
	color:#fff;
	background:#797979;
	font-size:1.5rem;
	width:3em;
	text-align:center;
	line-height:1.75em;	
}
	form{
		text-align:center;
		padding:1rem 0;
	}
input{
	font-size:1.5rem;
	padding:0 0.25em;
	line-height:2em;
	text-align:center;
	margin:0 0.5rem;
}

.roadara{
    background:#424242;
	background:#222;
	color:#fff;
	font-size:1rem;
}
.roadara p{
	padding:0;
	margin:0;
}
.roadara #rlbtn{
	padding:0.25em 0.5em;
	background:#fff;
	color:#424242;
	border-radius:3px;
	cursor:pointer;
	font-weight:bold;
}

.roadara #rlbtn::before{
	content:"●";
	margin-right:0.25em;
}
</style>
</body>
</html>
