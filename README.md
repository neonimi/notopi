## トピック掲示板「notopi」
### 説明
トピックを作成し、立てたトピックに対して記事を追加できる掲示板です。
ログインした人だけ投稿できます。

### 言語・環境
- 言語/フレームワーク： python/Django
- DB: sqlite3
- Webサーバー: Nginx
- APサーバー: WSGI

公開には、VPSサーバーを使用しています。

### アクセス制限
- 閲覧：なし（全員に表示）
- 投稿する：ユーザー登録者
- トピック作成する：ユーザー登録者

### セキュリティ対策
- 常時SSL化
- CSRF対策
CSRFの脆弱性に関する届出が、ウェブサイト届出全体に占める割合は、1パーセント未満と多くありませんが、CSRF攻撃による影響を受ける可能性があります。
ログイン機能があり、Cookieを用いたセッション管理を利用しているので、対策しました。

## 見え方
### トップ画面
<img width="350" alt="notopi_top" src="https://user-images.githubusercontent.com/32536597/146487658-9a4d9920-f7cb-4e27-b2b6-d0e554ecb2f0.png">

### 登録画面
<img width="350" alt="notopi_register" src="https://user-images.githubusercontent.com/32536597/146487668-dea94f2d-274f-42b5-b545-9ee50aeb3adc.png">

### ログイン画面
<img width="400" alt="notopi_login" src="https://user-images.githubusercontent.com/32536597/146487677-7cafcf0e-8437-4b74-8a67-b43914be44c2.png">

### トピック一覧画面
<img width="400" alt="notopi_topic" src="https://user-images.githubusercontent.com/32536597/146488493-703151ad-6d89-4c16-9733-eded09800617.png">

ユーザー：learn-test1がログインしました。<br>
ログインユーザーはトピックを作成できます。

### 記事一覧画面
<img width="400" alt="notopi_usertopic" src="https://user-images.githubusercontent.com/32536597/146488516-8a0be3d9-4d08-41e2-bbce-01a04f398774.png">

ログインユーザーは、立てたトピックに対して、投稿・編集ができます。
自分が投稿した記事にだけ、編集ボタンが表示されています。

### 記事編集画面
<img width="350" alt="notopi_edit" src="https://user-images.githubusercontent.com/32536597/146488529-d7591559-bc4b-4fed-b52c-07abd555d4c2.png">

### 問い合わせ画面
<img width="350" alt="notopi_contact" src="https://user-images.githubusercontent.com/32536597/146488540-912a054e-ca6a-4c70-a278-5a7fe5ea2e0e.png">

### エラー画面(500)
<img width="350" alt="notopi_error" src="https://user-images.githubusercontent.com/32536597/146488547-7c66e675-84a7-4cb6-ba42-ce3ece2e7cec.png">

エラーが発生した際の画面です。403,404,500のエラーページを配置しています。

### ログアウト画面
<img width="350" alt="notopi_logout" src="https://user-images.githubusercontent.com/32536597/146488466-da0ab5a1-024c-4116-81d0-46874aaa3872.png">
