# 事例4ページと体験版ページを共通のヘッダー・フッターで書き出す
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def head(title, p):
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{p}index.html"><img src="https://negilab.tokyo/logo.png" alt="ねぎラボ"></a>
    <nav class="nav">
      <a href="{p}index.html#cases">作って納めたもの</a>
      <a href="{p}index.html#how">進め方</a>
      <a href="{p}index.html#price">料金</a>
      <a href="{p}index.html#faq">よくある質問</a>
      <a class="btn btn-primary" href="{p}index.html#contact">作業の相談をする</a>
    </nav>
  </div>
</header>
<main>
'''


def foot(p):
    return f'''</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <img src="https://negilab.tokyo/logo.png" alt="ねぎラボ" style="height:28px">
        <p>ねぎラボ（neggy）／東京都杉並区／<a href="mailto:info@negilab.tokyo">info@negilab.tokyo</a><br>個人事業。適格請求書発行事業者（インボイス）未登録。</p>
      </div>
      <div>
        <h4>体験版一覧</h4>
        <ul>
          <li><a href="https://negilab.github.io/tools/pdfmask/">図面から名前と印を消す道具（パソコン向け）</a></li>
          <li><a href="https://negilab.github.io/tools/demo/shutten/">出店の受付（パソコン向け）</a></li>
          <li><a href="https://negilab.github.io/tools/demo/baito/">アルバイトの出勤と支払い（携帯でも）</a></li>
          <li><a href="https://negilab.github.io/tools/demo/nazotoki/">謎解き（携帯向け）</a></li>
          <li><a href="https://negilab.github.io/tools/douga/">簡単な動画編集の道具（音声・文字起こし・画面録画をひとつに。ねぎラボが自分で使っているもの）</a></li>
        </ul>
      </div>
      <div>
        <h4>くわしく</h4>
        <ul>
          <li><a href="{p}case/zumen/index.html">図面から名前と印を消す</a></li>
          <li><a href="{p}case/shutten/index.html">出店の受付</a></li>
          <li><a href="{p}case/arbeit/index.html">アルバイトの出勤と支払い</a></li>
          <li><a href="{p}case/nazotoki/index.html">謎解き</a></li>
        </ul>
      </div>
    </div>
    <p class="small">このフォームの内容は、ご返信のためだけに使います。サイトはGoogleアナリティクスで閲覧数を計測しています。© 2026 ねぎラボ</p>
  </div>
</footer>
</body>
</html>
'''


MAIL = 'mailto:info@negilab.tokyo?subject=%E4%BD%9C%E6%A5%AD%E3%81%AE%E7%9B%B8%E8%AB%87'


def case(slug, title, crumb, who, quote, items, demo_text, demo_url, cta):
    p = '../../'
    dl = '\n'.join(f'      <dt>{k}</dt>\n      <dd>{v}</dd>' for k, v in items)
    body = f'''<div class="wrap detail">
  <p class="crumb"><a href="{p}index.html">ねぎラボ</a> ／ 作って納めたもの：{crumb}</p>
  <section>
    <div class="case-head">
      <div class="case"><div class="who">{who}</div>
      <h1>「{quote}」</h1></div>
    </div>
    <dl>
{dl}
      <dt>体験版</dt>
      <dd>{demo_text}<br><a class="btn btn-primary" href="{demo_url}" style="margin-top:10px">体験版を開く→</a></dd>
    </dl>
    <div class="cta">
      <p>{cta}</p>
      <p><a class="btn btn-primary" href="{p}index.html#contact">作業の相談をする→</a></p>
      <p>メール：<a href="{MAIL}">info@negilab.tokyo</a></p>
    </div>
  </section>
</div>
'''
    out = os.path.join(ROOT, 'case', slug, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(head(title, p) + body + foot(p))


case('zumen', '図面から名前と印を消す道具｜ねぎラボ', '図面から名前と印を消す', '建設会社',
     '図面から名前と印を消すのに、1件2時間かかる',
     [('困りごと', '外に渡す前の図面から、工事名・所在地・設計者名・担当者名・電話番号・印を消す必要がありました。1物件で100ページ超、消す箇所は数千、印は全ページ。市販の墨消しソフトは語句は消せますが、探すのに1時間、印を塗るのに30分。1件2時間かかっていました。'),
      ('作ったもの', 'ブラウザで開くファイル1つです。開いて図面を読み込むと、消す候補が一覧に並びます。チェックを入れると、全ページから文字そのものが消えます。黒塗りではありません。印も消えます。138ページの図面で、読み込み40〜80秒、候補の一覧34秒、書き出し約4分です。'),
      ('どこで動くか', 'そのパソコンの中だけです。通信なし、ネット不要。図面は外に出ません。'),
      ('アプリの中のAI', '使っていません。')],
     '架空の図面でお試しいただけます。パソコンでご覧ください。',
     'https://negilab.github.io/tools/pdfmask/',
     '消す作業に限らず、「探して、1ページずつ直す」お仕事があれば、いまの書類をお見せください。')

case('shutten', '出店申し込みの受付を、ひとつの画面に｜ねぎラボ', '出店申し込みの受付', 'イベント運営会社',
     '出店の受付が、フォームとメールとパワポとエクセルに散らばっている',
     [('困りごと', 'Googleフォームに写真欄を付けると、Googleアカウントをお持ちの方しか開けません。そのため、写真だけ別のメールで受け取っていました。消防に出す配置図は、店名と写真をパワポに貼って作成。保健所に出す一覧表は、フォームの回答一覧から必要な列だけを抜き出して、エクセルに転記していました。'),
      ('お預かりしたもの', '既存のGoogleフォーム、保健所に出した一覧表1枚、消防に出した配置図1枚。'),
      ('作ったもの', '出店者の方はログインなしで、写真ごと申し込めます。申し込みは管理画面に表で並び、消防の配置図PDFと保健所の一覧表がボタンひとつで出せます。一斉メールも同じ画面から送れます。フォームを作る画面もあります。ご相談いただいた当日に、実際の受付で使い始めていただきました。作るのにかかったのは1日です。'),
      ('変えなかったこと', 'フォームの質問12問は、そのままです。'),
      ('どこで動くか', 'お客さまの会社のGoogleアカウントの中です。サーバ代はかかりません。'),
      ('アプリの中のAI', '使っていません。')],
     '架空のデータでお試しいただけます。パソコンでご覧ください。',
     'https://negilab.github.io/tools/demo/shutten/',
     '「受付は動いているけれど、そのあとの転記が手作業」でしたら、いまのフォームと、出している書類をお見せください。')

case('arbeit', 'アルバイトの出勤と支払いを、その会社のやり方のままアプリに｜ねぎラボ', 'アルバイトの出勤と支払い', 'イベント運営会社',
     'アルバイトの出勤と支払いを、一人ずつ時間×時給＋交通費で計算している',
     [('困りごと', '出勤と支払いを、エクセルに手で書きためていました。日ごとに誰が出たかを追い、一人ずつ時間×時給＋交通費を計算。当日の欠員や交代のたびに手で直すので、計算の食い違いが残っていました。月で締めたら、人ごとの明細を紙に印刷し、封筒に入れて手渡ししています。'),
      ('お預かりしたもの', '既存のエクセル1枚。'),
      ('作ったもの', '既製のソフトにやり方を合わせていただくのではなく、この会社の管理のやり方を、そのまま画面にしました。案件を作り、日を作り、その日に出た人を入れる。前の日と同じ顔ぶれなら、ボタン1つで写せます。交通費や駐車場代も、人ごとに持てます。月で締めたら「支払い明細」で人ごとの明細が出て、PDFにして送れます。封筒に入れて渡している紙が、これです。未払いは一覧で確認し、「支払済」で消し込みます。既存のエクセルから、案件11件・出勤の記録151行・名簿52人分を移し替えました。携帯からもお使いいただけます。'),
      ('どこで動くか', 'お客さまの会社のGoogleの中（アプリとスプレッドシート）です。外のコンピューターを借りる料金（サーバ代）はかかりません。'),
      ('アプリの中のAI', '使っていません。')],
     '架空のデータでお試しいただけます。パソコンでも携帯でも。体験版では、PDFの書き出しとメール送信はご利用いただけません。',
     'https://negilab.github.io/tools/demo/baito/',
     '「月末に一人ずつ計算して、紙にして渡している」のでしたら、そのエクセルと、お渡ししている紙をお見せください。')

case('nazotoki', '来場者向けの謎解きアプリ｜ねぎラボ', '来場者向けの謎解き', 'イベント運営会社',
     '問題を考える人も絵を描く人もいるのに、アプリを作る人だけいない',
     [('困りごと', '前回はLINEで一本道の謎解きを作られましたが、答えによる分岐が作れませんでした。問題を考える方、絵を描く方、運営の方はいらっしゃいます。アプリを作る人だけがいませんでした。'),
      ('作ったもの', '参加者は、QRを読んでログインなしで遊べる画面。運営の方は、パソコンで問題と分岐を線でつないで作る画面。結末は3つです。数百人が同時に始めても詰まらない作りです。本番前に試せる試験環境もあります。運営の方が作る画面は、すでにお使いいただいています。'),
      ('どこで動くか', 'お客さま向けに取得した独自ドメインと、Google Apps Scriptです。'),
      ('アプリの中のAI', '使っていません。')],
     '架空の題材で遊んでいただけます。携帯でご覧ください。',
     'https://negilab.github.io/tools/demo/nazotoki/',
     '「作る人だけいない」のでしたら、やりたいことを、そのままお聞かせください。前回の仕組みがLINEでも紙でも構いません。')


# 体験版一覧
def demo_item(name, desc, first, device, notes, url):
    rows = ''
    if first:
        rows += f'  <p><span class="label">まずここを</span>{first}</p>\n'
    if device:
        rows += f'  <p><span class="label">端末</span>{device}</p>\n'
    if notes:
        rows += f'  <p class="note">{notes}</p>\n'
    return f'''<div class="demo-item">
  <h3>{name}</h3>
  <p>{desc}</p>
{rows}  <a class="btn btn-primary" href="{url}">開く→</a>
</div>
'''


p = '../'
body = '''<div class="wrap">
<section>
<h1>体験版一覧</h1>
<p>作って納めたものと同じ画面を、架空のデータで触っていただけます。登録は不要です。携帯でお試しいただける2本、パソコン向けの2本の順に並べています。</p>
<h2>お客さまの業務のために作ったもの</h2>
'''
body += demo_item('アルバイトの出勤と支払い', '出勤した人にチェックを入れると、その日の支給額が出る画面です。',
                  '合言葉に「demo」と入力して入り、案件をひとつ開いてみてください。日ごとに出た人が並び、「＋ 人を足す」「前の日と同じ人にする」で顔ぶれを入れ替えられます。次に「支払い明細」で年月を選び、「明細を出す」を押すと、人ごとの明細が出ます。封筒に入れて渡している紙が、これです。',
                  '携帯でも、パソコンでも。',
                  'データは架空です。入力した内容は他の方には見えず、閉じると消えます。体験版では「PDFをダウンロード」「PDFをメールで送る」は動きません（押すと、その旨が表示されます）。',
                  'https://negilab.github.io/tools/demo/baito/')
body += demo_item('来場者向けの謎解き', '参加者がQRを読んで遊ぶ画面と、運営の方が問題を組み立てる画面です。',
                  '「参加者の画面」で、なまえを入れて始めてみてください。答えによって話が分かれます。運営の方が問題をつないで作る画面は、パソコンで「運営の画面」を開くとご覧いただけます。',
                  '参加者の画面は携帯向け。運営の画面はパソコン向け。',
                  '題材は架空です。入力した内容は他の方には見えず、閉じると消えます。',
                  'https://negilab.github.io/tools/demo/nazotoki/')
body += demo_item('図面から名前と印を消す', '外に渡す前の図面から、工事名・担当者名・電話番号・印を全ページまとめて消す道具です。',
                  'サンプル図面を読み込むと、消す候補の言葉が一覧に並びます。ひとつに「マスクする」のチェックを入れてみてください。その瞬間に、全ページから消えます。',
                  'パソコン向け。',
                  'サンプルは架空の建築図11ページで、物件名・会社名・人名・住所・電話・印はすべて作りものです。消す処理は納めたものと同じですが、体験版では書き出し（保存）はできません。お手元の図面を入れて試していただくこともできます。図面の中身とファイル名はこちらに送られません（このページを開いたときの記録と、サンプル図面の読み込みだけが通信です）。ご心配な場合は、サンプルでお試しください。',
                  'https://negilab.github.io/tools/pdfmask/')
body += demo_item('出店申し込みの受付', '出店者が写真つきで申し込む画面と、申し込みが表に並ぶ管理の画面です。',
                  '「出店者の画面」で写真をつけて申し込み、「管理の画面」に切り替えてみてください。いま送った申し込みが表に並び、消防の配置図と保健所の一覧表がボタンで出ます。',
                  'パソコン向け。',
                  'データは架空です。入力した内容は他の方には見えず、閉じると消えます。',
                  'https://negilab.github.io/tools/demo/shutten/')
body += '''<h2>自分のために作ったもの</h2>
<p>お客さまの業務ではなく、自分や家族のために作ったものの一部です。</p>
'''
body += demo_item('Swing Clipper', 'ゴルフの練習動画から、スイングの瞬間だけを自動で切り出します。見ていただくだけのデモです。', '', '', '',
                  'https://negilab.github.io/tools/demo/swing/')
body += demo_item('ひらがじゃん ヘルパー', '子どもと「ひらがな麻雀」をするときの助っ人です。手元の札を入れると、できる言葉とあがり方が出ます。', '', '', '',
                  'https://negilab.github.io/hiragajong-helper/')
body += demo_item('簡単な動画編集の道具', '動画から音声を取り出す、切り取る、重ねる、文字起こしをする。文字起こしにはAIを使い、その鍵はお使いになる方ご自身で入れていただきます。', '', '', '',
                  'https://negilab.github.io/tools/douga/')
body += f'''<div class="cta">
  <p>触ってみて「うちのあの作業も、こうなるか」と思われたら、その作業を一言でお送りください。ご相談も試作も無料です。</p>
  <p><a class="btn btn-primary" href="{p}index.html#contact">作業の相談をする→</a></p>
</div>
</section>
</div>
'''
out = os.path.join(ROOT, 'demo', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write(head('体験版一覧｜ねぎラボ', p) + body + foot(p))
