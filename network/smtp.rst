####
SMTP
####

SMTP (Simple Mail Transfer Protokoll) 
======================================

Um die Kommunikation mit einem Mailserver zu testen können folgende Befehle in einer telnet Sitzung benutzt werden.

.. code-block:: bash

 telnet mail.server.de 25
 
 helo <rechnername>
 auth login:
 username (base64 -> printf 'username' | mimencode)
 password (base64 -> printf 'password' | mimencode)
 mail from: <mein@mail.address>
 rcpt to: <empfänger@mail.address>
 Data
 To: mein Name <mein@mail.address>
 From: Empfänger Name <empfänger@mail.address>
 Subject: Hallo
 Dies ist eine telnet generierte Mail.
 .

Eine neue Zeile mit einem Punkt beendet die Dateneingabe und versendet die Mail. Jetzt kann überprüft werden ob die Mail beim Empfänger ankommt.
