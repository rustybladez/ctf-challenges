<?php
// Include the Image class and set the cookie before any HTML output
include 'classes/Image.php';

// Check if we need to set the cookie from the URL
if (isset($_GET['set_image'])) {
    setcookie('image_data', $_GET['set_image'], time() + 3600, "/");
    header("Location: view.php"); // Redirect to avoid URL parameter
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Photo</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('/background.jpg');
            background-size: cover;
            background-attachment: fixed;
            color: #f8f9fa;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }
        .view-container {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 2rem;
            border-radius: 10px;
            max-width: 700px;
            width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
        .card {
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        .hidden-content {
            display: none;
            color: #f8f9fa;
            background-color: #333;
            padding: 1rem;
            margin-top: 1rem;
            border-radius: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="view-container">
        <h1 class="mb-4">Photo Viewer</h1>
        <p class="mb-3">Enjoy this beautiful photo uploaded by our community members.</p>
        <div class="card">
            <?php
            // Retrieve and decode the cookie
            if (isset($_COOKIE['image_data'])) {
                $imageData = base64_decode($_COOKIE['image_data']);
                $imageObj = unserialize($imageData);

                if ($imageObj instanceof Image && file_exists($imageObj->path)) {
                    $mimeType = mime_content_type($imageObj->path);
                    if (strpos($mimeType, 'image/') === 0) {
                        // Display as an image if it's a valid image type
                        echo "<img src='" . htmlspecialchars($imageObj->path) . "' alt='Uploaded Image' style='width:100%; height:auto; border-radius:8px;'>";
                    } else {
                        // Display an error message but include file content
                        echo "<div class='alert alert-warning'>The image cannot be displayed or contains errors.</div>";
                        echo "<pre class='hidden-content'>" . htmlspecialchars(file_get_contents($imageObj->path)) . "</pre>";
                    }
                } else {
                    echo "<div class='alert alert-danger'>The file could not be displayed.</div>";
                }
            } else {
                echo "<div class='alert alert-danger'>No file specified.</div>";
            }
            ?>
        </div>
        <a href="index.php" class="btn btn-secondary mt-3">Back to Gallery</a>
    </div>
</body>
</html>
