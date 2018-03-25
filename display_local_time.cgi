#!/usr/bin/perl -wT

BEGIN {
  $| = 1;
  print "Content-type: text/html\n\n";
  use CGI::Carp('fatalsToBrowser');
}

use strict;
use warnings;
use CGI;

use CGI::Carp 'fatalsToBrowser'; #debugging only. security risk.

$ENV{"PATH"} = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin";

my $query = CGI->new();

my $localtime = `/bin/date` or die "unable to get the date: $!\r\n";

if($localtime =~ /\s+(\d{1,2}:\d{2}:\d{2})\s+/)
{
  $localtime = $1;
}

print $query->header("text/html"),
  $query->start_html(-title => "Local Time",
                     -bgcolor => "#ffffcc"),
  $query->p("The request time is $localtime"),
  $query->end_html;

