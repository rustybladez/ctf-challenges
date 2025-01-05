<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Photo Gallery</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
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
        .main-container {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 2rem;
            border-radius: 10px;
            max-width: 1000px;
            width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        .hero-section {
            background-color: rgba(0, 0, 0, 0.75);
            padding: 2rem;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        }
        .card {
            background-color: rgba(255, 255, 255, 0.9);
            border: none;
            overflow: hidden;
            transition: transform 0.2s;
        }
        .card:hover {
            transform: scale(1.05);
        }
        .card-img-top {
            height: 200px;
            object-fit: cover;
        }
    </style>
    <script>
        // JavaScript function to set the image_data cookie and redirect
        function viewImage(encodedData) {
            document.cookie = "image_data=" + encodedData + "; path=/";
            window.location.href = "view.php";
        }
    </script>
</head>
<body>
    <div class="main-container">
        <div class="hero-section">
            <h1 class="display-4">Welcome to My Christmas Photo Gallery</h1>
            <p class="lead">Discover and share beautiful holiday moments. Browse our gallery or add your own photos to inspire others.</p>
            <a href="upload.php" class="btn btn-primary btn-lg">
                <i class="fas fa-upload"></i> Upload a Photo
            </a>
        </div>
        
        <div class="gallery-container">
            <h2 class="text-center mb-4">Gallery</h2>
            <div class="row row-cols-1 row-cols-md-3 g-4">
                <?php
                include 'classes/Image.php';

                foreach (glob("images/*.*") as $filename) {
                    $image = new Image($filename);
                    $serializedImage = base64_encode(serialize($image));
                    echo "
                    <div class='col'>
                        <div class='card h-100'>
                            <img src='$filename' class='card-img-top' alt='" . basename($filename) . "'>
                            <div class='card-body text-center'>
                                <h5 class='card-title'>" . basename($filename) . "</h5>
                                <button onclick=\"viewImage('$serializedImage')\" class='btn btn-outline-primary'>
                                    <i class='fas fa-eye'></i> View
                                </button>
                            </div>
                        </div>
                    </div>";
                }
                ?>
            </div>
        </div>
    </div>
</body>
</html>
