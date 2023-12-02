# Readme 

## TR
Selenium ve BeautifulSoup4 kütüphanelerini kullanarak geliştirilen bir çekiliş botu programı, web tabanlı çekilişlerde otomatik katılım ve kazananın belirlenmesi amacıyla tasarlanmıştır. Bu bot, kullanıcının belirlediği bir YouTube canlı yayınının sohbet bölümündeki katılımcıları izleyerek belirli bir kelime veya ifade içeren mesajları tespit eder ve bu katılımcıları bir set içinde toplar.

Program, Selenium'u kullanarak web tarayıcısını otomatik olarak başlatır, belirtilen YouTube canlı yayınının sohbet bölümündeki mesajları çeker ve BeautifulSoup4 kütüphanesi ile bu mesajları parse eder. Belirli bir kelime veya ifade içeren mesajları bulan program, bu mesajlara ait kullanıcıları bir set içinde saklar. Çekilişin sonunda ise bu set içinden rastgele bir kullanıcıyı seçerek kazananı belirler.

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


## EN
This Python program is designed for automated participation and winner selection in web-based raffles using the Selenium and BeautifulSoup4 libraries. The bot monitors participants in the chat section of a user-specified YouTube live stream, detects messages containing specific keywords or expressions, and gathers these participants in a set.

## Usage of Selenium and BeautifulSoup4:
- The web browser is automatically launched using 'Selenium'.
- The 'BeautifulSoup4' library is employed to parse HTML content.

## Message Filtering:
- Users can specify a keyword or expression to identify participants in the raffle.
- Storage of Participants:
- Information about participants in the raffle, those who send messages meeting certain criteria, is stored in a Python set.

## Conclusion of the Raffle and Winner Determination:
- The raffle is concluded after a certain period or when a specific number of participants is reached.
- At the end of the raffle, a winner is determined by randomly selecting an individual from the set of stored participants.

## Automatic Updates (Optional):
- The program can periodically check the chat to monitor new participants. This ensures equal opportunities for everyone interested in joining the raffle.
