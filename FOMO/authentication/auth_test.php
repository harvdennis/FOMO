<?php 

define ("DEVELOPER_URL", "http://studentnet.cs.manchester.ac.uk/authenticate/auth_test.php");

define("AUTHENTICATION_SERVICE_URL", "http://studentnet.cs.manchester.ac.uk/authenticate/");

define("AUTHENTICATION_LOGOUT_URL", "http://studentnet.cs.manchester.ac.uk/systemlogout.php");

require_once("Authenticator.php");

session_start();

Authenticator::requireStudyLevel();

Authenticator::validateUser();
?>

<html>
    <head>
        <title>Login</title>

    </head>
    <body>
    <ul>
            <li>
                You authenticated at 
                    <?php
                        $timestamp = Authenticator::getTimeAuthenticated();
                        echo date("l jS F Y H:i:s", $timestamp);
                    ?>
            </li>
            
            <li>
                Your username is 
                    <?php
                        echo Authenticator::getUsername();
                    ?>
            </li>
            
            <li>
                Your full name is 
                    <?php
                        echo Authenticator::getFullName();
                    ?>
            </li>
            
            <li>
                Your user category is 
                    <?php
                        echo Authenticator::getUserCategory();
                    ?>
            </li>            
            
            <li>
                Your department is 
                    <?php
                        echo Authenticator::getUserDepartment();
                    ?>
            </li>                 
            
            <li>
                Your year of study (not retrieved by default - see below) is
                    <?php
                        echo Authenticator::getStudyLevel();
                    ?>
            </li>                 
            
        </ul>
    </body>
</html>