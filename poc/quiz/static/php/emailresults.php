<?php
// the message
$msg = "First line of text\nSecond line of text";

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("someone@example.com","My subject",$msg);
?>
<<<<<<< Updated upstream
<<<<<<< Updated upstream

=======
<!-- adding the php to the html page
    <form name="emailresultsform" method="post" action="emailresults.php"> -->
>>>>>>> Stashed changes
=======
<!-- adding the php to the html page
    <form name="emailresultsform" method="post" action="emailresults.php"> -->
>>>>>>> Stashed changes

<?php $yourname		= $_POST['yourname'];
$youremail		= $_POST['youremail'];
$welcomecopy	= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">Thank you for taking the Waterloo Engineering Type Quiz. We hope you find your results helpful.<br /><br />Your responses indicate that you might want to consider these Waterloo Engineering programs:</p>';
$onetitle		= '<div style="border:1px solid #ccc;padding:10px;width:780px;"><p style="font-family:Verdana, Helvetica, Arial, sans-serif;font-size:16px;font-weight:bold;color:#57068C;margin-bottom:-5px;">' . $_POST['onetitle'] . '</p>';$onelink		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['onelink'] . '</p>';
$onecopy		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['onecopy'] . '</p></div>';$twotitle		= '<div style="border:1px solid #ccc;padding:10px;width:780px;"><p style="font-family:Verdana, Helvetica, Arial, sans-serif;font-size:16px;font-weight:bold;color:#57068C;margin-bottom:-5px;">' . $_POST['twotitle'] . '</p>';
$twolink		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['twolink'] . '</p>';$twocopy		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['twocopy'] . '</p></div>';$threetitle		= '<div style="border:1px solid #ccc;padding:10px;width:780px;"><p style="font-family:Verdana, Helvetica, Arial, sans-serif;font-size:16px;font-weight:bold;color:#57068C;margin-bottom:-5px;">' . $_POST['threetitle'] . '</p>';
$threelink		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['threelink'] . '</p>';$threecopy		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">' . $_POST['threecopy'] . '</p></div>';$findoutmore	= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;"><strong>Find out more:</strong></p>';
$linkone		= '<p style="font-family:Verdana, Helvetica, Arial, sans-serif;">For more information about Waterloo Engineering Admissions: <a href="https://uwaterloo.ca/engineering/future-undergraduate-students/application-process">https://uwaterloo.ca/engineering/future-undergraduate-students/application-process</a>';
$linktwo		= 'For students interested in Waterloo Architecture: <a href="http://www.architecture.uwaterloo.ca">http://www.architecture.uwaterloo.ca</a>';$linkthree		= 'Request a Brochure: <a href="https://uwaterloo.ca/future-students/request-brochures">https://uwaterloo.ca/future-students/request-brochures</a>';
$linkfour		= 'Contact Us: <a href="mailto:enginfo@uwaterloo.ca">enginfo@uwaterloo.ca</a></p>';
$uwatlogo		= '<div style="width:800px;height:40px;position:relative;background-color:#000;"><img src="http://uwaterloo.ca/images/template/uw_wordmark.gif" /></div>';
$headers  = "MIME-Version: 1.0\r\n"; 
$headers .= "Content-type: text/html; charset=iso-8859-1\r\n";
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 1) Edit the first line below to match your email address////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
$headers .= "From: Engineering @ The University of Waterloo <> \n";
$headers .= "Reply-To: admissions@engmail.uwaterloo.ca \n\n";
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 2) Then edit the following two lines to match your site name and email address////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
$siteName		= "engineering.uwaterloo.ca";
$to 			= $youremail;
$toSubject 		= "Here are $yourname's results from $siteName";
$emailBody 		= "$uwatlogo $welcomecopy $onetitle $onelink $onecopy <br />$twotitle $twolink $twocopy <br />$threetitle $threelink $threecopy <br /><br />$findoutmore $linkone <br />$linktwo <br />$linkthree <br />$linkfour";
$message 		= $emailBody;
echo "Result have been emailed to $youremail";
mail($to, $toSubject, $message, $headers);?>
