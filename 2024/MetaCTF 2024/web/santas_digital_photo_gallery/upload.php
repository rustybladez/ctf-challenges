<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload a Photo</title>
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
        .upload-container {
            background-color: rgba(0, 0, 0, 0.8);
            padding: 2rem;
            border-radius: 10px;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="upload-container">
        <h1 class="mb-4">Upload a Photo</h1>
        <p class="mb-3">
            Thank you for sharing your photos! Our gallery is a collection of images from our community, open to everyone. Please follow the guidelines below to ensure your photo is suitable for our gallery.
        </p>
        <ul class="text-start mb-4" style="padding-left: 1.5rem;">
            <li>Supported formats: JPEG, PNG, or GIF.</li>
            <li>Maximum file size: 5MB.</li>
            <li>Only family-friendly, appropriate content, please.</li>
        </ul>
        <form action="upload.php" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <input type="file" name="image" accept="image/*" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-success btn-lg mb-3">
                <i class="fas fa-upload"></i> Upload Photo
            </button>
        </form>
        <?php
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $target_dir = "images/";
            $target_file = $target_dir . basename($_FILES["image"]["name"]);
            if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
                echo "<div class='alert alert-success mt-3'>Your photo has been uploaded! Visit the gallery to see it.</div>";
            } else {
                echo "<div class='alert alert-danger mt-3'>There was an error uploading your file. Please try again.</div>";
            }
        }
        ?>
        <a href="index.php" class="btn btn-secondary mt-3">Back to Gallery</a>
    </div>
</body>
</html>
