from MusicKen.config import ASSISTANT_NAME, OWNER, PROJECT_NAME


class Messages:
    HELP_MSG = [
        ".",
        f"""
**👋🏻 Merhaba sayfasına tekrar hoşgeldiniz [{PROJECT_NAME}]

⚪️ {PROJECT_NAME} sesli sohbetlerde music çalıyorum

⚪️ Assistant Name >> @{ASSISTANT_NAME}\n\n☑️ asistanı gruba ekleyin 
   Sahibim; @GOLGENDEIZIMVARR
Asistan;  @Sancakbeyasistan
Grubumuz; @sohbetsancakbeyi **
""",
        f"""
**🛠️ Pengaturan**


1) Botu Kanal Yöneticisi Yap
2) /userbotjoinchannel'ı Bağlantılı Grupta Gönder
3) Şimdi Bağlı Grupta Komut Gönder
""" ,
        f"""
**🔰 Komutlar**
**=>> Şarkı Çalma **
• /oynat (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /ytplay (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /yt (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /p (şarkı adı) - İstediğiniz şarkıyı youtube üzerinden çalmak için
• /lplay - gc'deki yanıtlanan şarkılar vcg'de otomatik olarak oynatılacaktır
• /player: Oynatıcı ayarları menüsünü açın
• /atla: Geçerli parçayı atlar
• /durdur: Parçayı duraklat
• /devam: Duraklatılan bir parçayı devam ettirir
• /son: Medya oynatmayı durdurur
• /current: Çalmakta olan parçayı görüntüler
• /playlist: Bir çalma listesi görüntüler
Komut /player /skip /pause /resume /end Hariç Tüm Komutlar Yalnızca Grup Yöneticileri İçin Kullanılabilir
**==>>Şarkıyı İndir **
• /bul [şarkı adı]: youtube'dan şarkı sesini indirin
""" ,
        F"""
***=>> Müzik Çalma Kanalı **
️ Yalnızca bağlantılı grup yöneticileri için:
• /cplay (şarkı adı) - istediğiniz şarkıyı çal
• /cplaylist - Çalmakta olan listeyi göster
• /cccurrent - Şu anda oynatılanı göster
• /cplayer - müzik çalar ayarları panelini aç
• /cpause - şarkı çalmayı duraklat
• /cresume - şarkı çalmaya devam etme
• /cskip - sonraki şarkıyı çal
• /cend - müzik çalmayı durdur
• /userbotjoinchannel - asistanları sohbetinize davet edin
️ Bağlantılı Gruplarda Oynamayı Sevmiyorsanız:
1) Kanal Kimliğinizi alın.
2) Başlıklı Bir Grup Oluşturun: Müzik Kanalı: YOUR_CHANNEL ID
3) Botu Tam İzinle Kanal Yöneticisi Olarak Ekle
4) Kanala yönetici olarak @ { ASSISTANT_NAME } ekleyin .
5) Sadece Grubunuza Sipariş Gönderin
***=>> Daha Fazla Araç **
- /admincache: Grup Yönetici Bilgilerinizi güncelleyin. Bot Yöneticiyi Tanımıyorsa Deneyin
- /userbotjoin: @ { ASSISTANT_NAME } Userbot'u Grubunuza Davet Edin
""" ,
        f"""👋🏻 Merhaba, Benim adım [ { PROJECT_NAME } ]
❤
️ Şarkıları sevenler için bir çok özelliğim var
Grupta şarkı çal 
Kanaldaki şarkıları çal
Şarkıları indir
youtube linkleri arıyorum
❤
️ Daha fazla bilgi için yardım düğmesine tıklayın
""" ,
    ]
