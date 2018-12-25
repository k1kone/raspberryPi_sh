<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>test</title>
</head>
<body>
<div class="wrap">
    <header>header
    <nav>
        <ul>
            %for i, j in navlis.items():
                <li><a href="{{j}}">{{i}}</a></li>
            %end
        </ul>
    </nav>
    </header>
    <article>
        <p>{{mod}}</p>
        <p>{{dht}}</p>
        <p>{{modtxt}}<br>{{modtxt2}}</p>
        <p>{{ntime}}</p>
    </article>
    <footer>copyright</footer>
</div>
<script>
    window.onload = function(){
            setTimeout('location.reload()', 5000);
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


