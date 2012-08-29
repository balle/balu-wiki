#####
HTML5
#####

Basics
=======

.. code-block:: html5

<!DOCTYPE html>
<html>
  <head>
    <title>HTML5 / CSS3 Spielplatz</title>
  </head>
  <body>
    <header>Dies ist die &UUml;berschrift</header>
    <nav><a>Link1|</a><a>Link2</a></nav>
    
    <section>
      <header>Artikel&uuml;berschrift</header>
      <p>Ganz viel tolles Bla Bla</p>
      <aside>Eine Randnotiz</aside>
    </section>

    <footer>Dies ist die Fussnote</footer>
  </body>
</html>


Forms
=====

.. code-block:: html5

    <form>
      <fieldset>
        <legend>HTML5 form</legend>
        <p>
          <label for="email">E-Mail</label>
          <input type="email" placeholder="E-Mail" id="email" />
        </p>
        <p><input type="url" placeholder="URL" /></p>
        <p><input type="tel" placeholder=="Phone"/></p>
        <p><input type="search" placeholder="Searchfield" /></p>
        <p><<input type="range" placeholder="Range" /></p>
        <p><input type="number" placeholder=="Number" /></p>
        <p><input type="date" placeholder="Date" /></p>
        <p><input type="datetime" placeholder="DateTime" /></p>
        <p><input type="color" placeholder="color" autofocus /></p>
      </fieldset>
    </form>
