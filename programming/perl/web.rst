##########
Web stuff
##########

Manipulate cookies
==================

.. code-block:: perl

  perl -MLWP::UserAgent -e '$a = LWP::UserAgent->new(useragent => "yoo 1.3"); \
  $r = HTTP::Request->new(GET => $ARGV[0]); \
  $r->header("Cookie" => "$ARGV[1]=$ARGV[2]"); \
  print $a->request($r)->content;' \
  http://some.site key value


Read HTTP headers
==================

.. code-block:: perl

  perl -MLWP::UserAgent -e '$a = LWP::UserAgent->new(useragent => "fooblah 1.0"); \
  $r = $a->get($ARGV[0]); \
  map { print "$_:" . $r->header("$_") . "\n"; } $r->header_field_names;' \
  http://www.chaostal.de

