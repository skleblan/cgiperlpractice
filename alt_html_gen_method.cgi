#!/usr/bin/perl -wT
use strict;
use CGI;

my $query = new CGI;

print $query->header("text/html");
print <<END_HERE;
<html><head><title>My Second First CGI Script</title></head>
<body bgcolor="#ffffcc">

<h1>This is a pretty lame web page again</h1>
<p>Who is this Ovid guy, anyway?</p>
<p>This page was generated as a "here" document</p>
</body></html>
END_HERE
