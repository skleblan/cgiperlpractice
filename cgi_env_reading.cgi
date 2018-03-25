#/usr/bin/perl -wT
use strict;
use CGI;

my $query = CGI->new();

print $query->header("text/html"),
  $query->start_html(-title => "My First CGI Script",
                     -bgcolor => "#ffffcc");

print $query->h1("Here is a list of CGI Environment variables");

print $query->p("This also has a mix of printing with and without ".
  "an object reference.");

foreach my $key (sort(keys(%ENV)))
{
  print "$key = $ENV{$key}<br/>\n";
}

print $query->end_html;

