<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>setting</title>
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
        <form action="" method="POST">
            <input type="number" name="time_h" min=0 max=23 />
            <input type="number" name="time_m" min="0" max="59" step="10" />
            <input type="submit" value="登録"/>
        </form>
    </article>
    <footer>copyright</footer>
</div>
</body>
</html>