#/usr/bin/perl -wT
use strict;
use CGI;

my $query = CGI->new();

print $query->header("text/html"),
  $query->start_html(-title => "My First CGI Script",
                     -bgcolor => "#ffffcc"),
  $query->h1("This is a pretty lame web page"),
  $query->p("Who is this Zebra guy, anyway?"),
  $query->end_html;

