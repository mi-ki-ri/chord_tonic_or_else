# TONIC OR ELSE

## Description

このコードは、音楽理論に基づいて和音（コード）を分類するためのものです。具体的には、和音を「ドミナント（Dominant）」、「サブドミナント（Subdominant）」、「サブドミナント・マイナー（Subdominant-Minor）」の 3 つのカテゴリに分類します。

まず、subdominant_minor_list と dominant_list という 2 つの空のリストが定義されています。これらのリストは、それぞれサブドミナント・マイナーとドミナントの和音を格納するためのものです。

次に、12 回のループが実行されます。このループの中で、appendixes というリストの各要素に対してさらにループが実行されます。各ループの中で、curent_chord という変数に現在のベース和音（bass_chord.chord）と appendix を結合したものが代入されます。この curent_chord は現在の和音を表しています。

その後、curent_chord が出力され、Chord(curent_chord).components()メソッドを使ってその和音の構成音が出力されます。

次に、条件分岐が行われます。もし和音の構成音に「F」と「B」が含まれている場合、その和音は「ドミナント」として分類され、dominant_list に追加されます。もし「F」のみが含まれている場合、その和音は「サブドミナント」として分類され、subdominant_list に追加されます。最後に、もし「Ab」が含まれている場合、その和音は「サブドミナント・マイナー」として分類され、subdominant_minor_list に追加されます。

このコードは、和音の分類を自動化するためのものであり、音楽理論に基づいた和音の分析を行う際に役立ちます。
