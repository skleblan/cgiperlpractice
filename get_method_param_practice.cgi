#/usr/bin/perl -wT
use strict;
use warnings;
use CGI;

my $query = CGI->new();

#my @names = $query->param; #gets all keys of key-value pairs.

my $output_string;

my $user_param = $query->param("user");

print $query->header("text/html"),
  $query->start_html(-title => "Sample GET method input",
                     -bgcolor => "#ffffcc"),
  $query->h1("Sample GET method input"),
  $query->p("Accepting parameter input for \"user\"");

if($user_param =~ /^(\w+)$/)
{
  print $query->p("request was submitted for user $1");
}

print $query->end_html;

