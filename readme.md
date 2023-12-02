# Readme 

## TR
Bu Python programı, Selenium ve BeautifulSoup4 kütüphanelerini kullanarak geliştirilmiş bir çekiliş botu. Program, YouTube canlı yayınlarının sohbet bölümündeki katılımcıları izleyerek belirli bir kelime içeren mesajları tespit ediyor ve bu katılımcıları bir set içinde saklıyor. İşte programın temel özellikleri:

## Selenium ve BeautifulSoup4 Kullanımı:
- `Selenium` kullanılarak web tarayıcısı otomatik olarak başlatılır.
- `BeautifulSoup4` kütüphanesi, HTML içeriğini parse etmek için kullanılır.

## Mesaj Filtreleme:
- Kullanıcı, çekilişe katılanları belirlemek için belirli bir kelime veya ifade belirleyebilir.

## Katılımcıların Saklanması:
- Çekilişe katılan kullanıcıların bilgileri, belirli kriterlere uyan mesajları gönderenler, bir Python set içinde saklanır.

## Çekilişin Sonlandırılması ve Kazananın Belirlenmesi:
- Belirli bir süre veya belirli bir katılımcı sayısına ulaşıldığında, çekiliş sonlandırılır.
- Çekiliş sonunda, toplu halde saklanan katılımcılar içinden rastgele bir kişi seçilerek kazanan belirlenir.

## Otomatik Güncelleme (Opsiyonel):
- Program, belirli aralıklarla sohbeti kontrol ederek yeni katılımcıları izleyebilir. Bu sayede, çekilişe katılmak isteyen herkesin fırsat eşitliği sağlanır.

Bu çekiliş botu, kullanıcı dostu bir arayüzle çekilişlerin otomatik ve adil bir şekilde yapılmasını sağlar. Programın özelleştirilebilir yapısı, kullanıcılara çeşitli seçenekler sunarak çekiliş deneyimini kişiselleştirmelerine olanak tanır.

## EN
This Python program is designed for automated participation and winner selection in web-based raffles using the Selenium and BeautifulSoup4 libraries. The bot monitors participants in the chat section of a user-specified YouTube live stream, detects messages containing specific keywords or expressions, and gathers these participants in a set.

## Usage of Selenium and BeautifulSoup4:
- The web browser is automatically launched using Selenium.
- The BeautifulSoup4 library is employed to parse HTML content.

## Message Filtering:
- Users can specify a keyword or expression to identify participants in the raffle.
- Storage of Participants:
- Information about participants in the raffle, those who send messages meeting certain criteria, is stored in a Python set.

## Conclusion of the Raffle and Winner Determination:
- The raffle is concluded after a certain period or when a specific number of participants is reached.
- At the end of the raffle, a winner is determined by randomly selecting an individual from the set of stored participants.

## Automatic Updates (Optional):
- The program can periodically check the chat to monitor new participants. This ensures equal opportunities for everyone interested in joining the raffle.
