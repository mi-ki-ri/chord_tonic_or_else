# TONIC OR ELSE

## Description

このコードは、音楽理論に基づいて和音（コード）を分類するためのものです。具体的には、和音を「ドミナント（Dominant）」、「サブドミナント（Subdominant）」、「サブドミナント・マイナー（Subdominant-Minor）」の 3 つのカテゴリに分類します。

まず、subdominant_minor_list と dominant_list という 2 つの空のリストが定義されています。これらのリストは、それぞれサブドミナント・マイナーとドミナントの和音を格納するためのものです。

次に、12 回のループが実行されます。このループの中で、appendixes というリストの各要素に対してさらにループが実行されます。各ループの中で、curent_chord という変数に現在のベース和音（bass_chord.chord）と appendix を結合したものが代入されます。この curent_chord は現在の和音を表しています。

その後、curent_chord が出力され、Chord(curent_chord).components()メソッドを使ってその和音の構成音が出力されます。

次に、条件分岐が行われます。もし和音の構成音に「F」と「B」が含まれている場合、その和音は「ドミナント」として分類され、dominant_list に追加されます。もし「F」のみが含まれている場合、その和音は「サブドミナント」として分類され、subdominant_list に追加されます。最後に、もし「Ab」が含まれている場合、その和音は「サブドミナント・マイナー」として分類され、subdominant_minor_list に追加されます。

このコードは、和音の分類を自動化するためのものであり、音楽理論に基づいた和音の分析を行う際に役立ちます。

## 期待される結果

```python
===================================
Tonic List
['C', 'Cm', 'Cmaj7', 'C7', 'Cm7', 'Csus2', 'Cdim', 'Cdim7', 'Cm7b5', 'Dbdim', 'Dbdim7', 'Dbm7b5', 'D', 'Dmaj7', 'D7', 'Dsus4', 'Dsus2', 'Daug', 'Eb', 'Ebm', 'Ebmaj7', 'Eb7', 'Ebm7', 'Ebaug', 'Ebdim', 'Ebdim7', 'Ebm7b5', 'E', 'Em', 'Emaj7', 'E7', 'Em7', 'Esus4', 'Esus2', 'Eaug', 'Edim', 'Edim7', 'Em7b5', 'Gb', 'Gbm', 'Gb7', 'Gbm7', 'Gbsus4', 'Gbaug', 'Gbdim', 'Gbdim7', 'Gbm7b5', 'G', 'Gm', 'Gmaj7', 'Gsus4', 'Gsus2', 'Gaug', 'Gdim', 'Gdim7', 'A', 'Am', 'Amaj7', 'A7', 'Am7', 'Asus4', 'Asus2', 'Adim', 'Adim7', 'Am7b5', 'Bbaug', 'Bbdim', 'Bbdim7', 'B', 'Bm', 'Bmaj7', 'B7', 'Bm7', 'Bsus4', 'Bsus2', 'Baug']
Subdominant List
['Csus4', 'Db', 'Dbmaj7', 'Dbaug', 'Dm', 'Dm7', 'Ddim', 'Dm7b5', 'Ebsus2', 'F', 'Fm', 'Fmaj7', 'F7', 'Fm7', 'Fsus4', 'Fsus2', 'Faug', 'Gbmaj7', 'Gm7', 'Gm7b5', 'Aaug', 'Bb', 'Bbm', 'Bbmaj7', 'Bb7', 'Bbm7', 'Bbsus4', 'Bbsus2']
Subdominant Minor List
['Caug', 'Dbm', 'Dbm7', 'Dbsus4', 'Dbsus2', 'Ebsus4', 'Gbsus2', 'Ab', 'Abm', 'Abmaj7', 'Ab7', 'Abm7', 'Absus4', 'Absus2', 'Abaug', 'Abdim', 'Abm7b5', 'Bbm7b5']
Dominant List
['Db7', 'Ddim7', 'Fdim', 'Fdim7', 'Fm7b5', 'G7', 'Abdim7', 'Bdim', 'Bdim7', 'Bm7b5']
```
