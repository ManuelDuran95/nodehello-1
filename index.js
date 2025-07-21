import express from 'express';
const app = express();

app.get('/', (req, res) => {
  const name = process.env.NAME || 'World w2';
  res.send(`Hello ${name}!`);
});

const port = parseInt(process.env.PORT) || 8080;
app.listen(port, () => {
  console.log(`helloworld: listening on port ${port}`);
});
