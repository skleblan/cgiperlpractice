#!/usr/bin/perl -wT

BEGIN {
  $| = 1;
  print "Content-type: text/html\n\n";
  use CGI::Carp('fatalsToBrowser');
}

use strict;
use warnings;
use CGI;

$ENV{"PATH"} = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin";

my $query = CGI->new();

my $process_list = "Data not yet retrieved\n";

open PS_HANDLE, "ps aux|";
my @process_output = <PS_HANDLE>;
close PS_HANDLE;

my @users = ();

for my $line (@process_output)
{
  if($line =~ /^(\w+)\s+/ and )
  {
