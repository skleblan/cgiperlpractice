#!/usr/bin/perl
use strict;
use CGI qw/:standard/;

print header,
  start_html( "-title" => "Log in to Weird Sports"),
  div({ -align=>"center",
      -style=>"color:#000000; font-family: Tahoma, helvetica, arial;"},
    h1("Log in to your account"),
    p("Here you can log in to the Weird Sports mailing list archives. ".
      "In theory, you will be able to change your user settings.  In reality".
      ", however, you can't bc this is just an example from a ".
      a( { -href => "index.html" },
        "studpid CGI programming course" ), "." ),

    start_form({ -action => "login_weird_sports.cgi",
                 -enctype => "application/x-www-form-urlencoded",
                 -method => "post" }),
    table({ -bgcolor => "#000000",
            -border => "0",
            -cellpadding => "2",
            -cellspacing => "1",
            -style => "font: 10pt;" },
          Tr( { -style => "background-color:#CCCCCC" },
            td( strong( "User Name:" ) ),
            td( input( { -maxlength => "30",
                         -name      => "username",
                         -size      => "30",
                         -type      => "text"} )
            ) # end td
          ), # end Tr
          Tr( { -style => "background-color:#CCCCCC"},
            td( strong( "Password:" ) ),
            td( input( { -maxlength => "30",
                         -name      => "password",
                         -size      => "30",
                         -type      => "password"} )
            ) # end td
          ), # end Tr
          Tr(
            td( { -colspan => "2",
                  -style   => "background-color:#CCCCCC" },
                input ( { -name => "remember",
                          -type => "checkbox"} ),
                " Remember my ID on this computer. ",
            ) # end td
          ), # end Tr
      ), #end table

     p( input({ -type => "submit",
                -value => "Login"}),
         " ",
         input( { -type => "reset"} ),
     ), #end p

     end_form,
  ), #end div

  end_html;

