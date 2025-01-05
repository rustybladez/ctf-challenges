const http = require('http');
const url = require('url');
const fs = require('fs');
const path = require('path');

const sendFile = (res, filePath, replacements = {}) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      res.writeHead(500, { 'Content-Type': 'text/html' });
      res.end('<h1>Server Error</h1>');
      return;
    }

    let content = data;
    for (const [key, value] of Object.entries(replacements)) {
      content = content.replace(new RegExp(`{{${key}}}`, 'g'), value);
    }

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(content);
  });
};

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/' && req.method === 'GET') {
    return sendFile(res, path.join(__dirname, 'index.html'));
  } else if (parsedUrl.pathname === '/flag' && req.method === 'GET') {
    try {
      let y = parsedUrl.query.y;
      if (y == null) {
        return sendFile(res, path.join(__dirname, 'null.html'));
      }
      if (y.length > 17) {
        return sendFile(res, path.join(__dirname, 'no-flag.html'));
      }
      let x = BigInt(parseInt(y));
      if (x < y) {
        let flag = fs.readFileSync("flag.txt", 'utf8')
        return sendFile(res, path.join(__dirname, 'flag.html'), {flag});
      }
      return sendFile(res, path.join(__dirname, 'no-flag.html'));
    } catch (e) {
      console.log(e)
      return sendFile(res, path.join(__dirname, "error.html"));
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/html' });
    return sendFile(res, path.join(__dirname, '404.html'));
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
