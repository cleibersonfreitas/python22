from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Academia Cruzmaltina</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background-color: #fff;
      color: #000;
    }
    header {
      background-color: #000;
      color: white;
      padding: 20px;
      text-align: center;
    }
    nav {
      background-color: #e30613;
      display: flex;
      justify-content: center;
      gap: 20px;
      padding: 10px;
    }
    nav a {
      color: white;
      text-decoration: none;
      font-weight: bold;
    }
    section {
      padding: 40px 20px;
    }
    .container {
      max-width: 1000px;
      margin: 0 auto;
    }
    .grid {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }
    .card {
      flex: 1 1 calc(33% - 20px);
      border: 1px solid #ccc;
      border-radius: 10px;
      overflow: hidden;
      background-color: #f9f9f9;
    }
    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }
    .card h3 {
      margin: 10px;
    }
    .card p {
      margin: 10px;
    }
    .imc-container {
      background-color: #f1f1f1;
      padding: 30px;
      border-radius: 10px;
      text-align: center;
    }
    .imc-container input {
      padding: 10px;
      margin: 10px;
      width: 200px;
    }
    .imc-container button {
      padding: 10px 20px;
      background-color: #e30613;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .imc-container button:hover {
      background-color: #c00410;
    }
    footer {
      background-color: #000;
      color: white;
      text-align: center;
      padding: 20px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Academia Cruzmaltina</h1>
    <p>Força, Garra e Tradição Vascaína</p>
  </header>

  <nav>
    <a href="#aulas">Aulas</a>
    <a href="#professores">Professores</a>
    <a href="#loja">Loja de Suplementos</a>
    <a href="#imc">Calculadora IMC</a>
  </nav>

  <section class="container" id="aulas">
    <h2>Aulas Oferecidas</h2>
    <div class="grid">
      <div class="card">
        <img src="https://www.chrissports.com.br/aulas-de-danca/imagens/quanto-custa-aula-de-musculacao-para-iniciantes.jpg" alt="Musculação">
        <h3>Musculação</h3>
        <p>Ganhe força e resistência com treinos personalizados.</p>
      </div>
      <div class="card">
        <img src="https://marjan.com.br/wp-content/uploads/2022/03/treino-crossfit.jpg" alt="Crossfit">
        <h3>Crossfit</h3>
        <p>Alta intensidade para transformar seu corpo.</p>
      </div>
      <div class="card">
        <img src="https://tecnofit-site.s3.sa-east-1.amazonaws.com/media/files/2023/11/17103714/equipamentos-studio-pilates-scaled.jpg" alt="Pilates">
        <h3>Pilates</h3>
        <p>Flexibilidade e equilíbrio com foco na respiração.</p>
      </div>
    </div>
  </section>

  <section class="container" id="professores">
    <h2>Nosso Time de Professores</h2>
    <div class="grid">
      <div class="card">
        <img src="https://admin.cnnbrasil.com.br/wp-content/uploads/sites/12/2025/02/caike-pro-fisiculturista-e1739373554777.jpeg?w=640" alt="Carlos">
        <h3>Carlos Oliveira</h3>
        <p>Especialista em musculação e hipertrofia.</p>
      </div>
      <div class="card">
        <img src="https://img.freepik.com/fotos-premium/apta-jovem-morena-instrutora-de-pilates-mostrando-diferentes-exercicios-em-um-fundo-branco-uma-esteira_255667-52692.jpg" alt="Aline">
        <h3>Aline Souza</h3>
        <p>Instrutora de Pilates e alongamento funcional.</p>
      </div>
      <div class="card">
        <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRW6QooFhEu5K82TwnK01o0dzoLYJjl8OuFlAkNVuQPUGsYefcG6A3QNYZ7K1zdgSZdvc31kHISnhvoRog9MvLERh9V_lGPYHdXkNlerIyroBVsnq0Ywo_BnmOfQTfg04XU7vW2S_RMQasdZ1zxvCRXcYxGGtMY44QdA3zm-JOFspFE1ouP5HstAF-/s953/unnamed%20(95).jpg" alt="Renato">
        <h3>Renato Silva</h3>
        <p>Coach de Crossfit certificado e ex-atleta vascaíno.</p>
      </div>
    </div>
  </section>

  <section class="container" id="loja">
    <h2>Loja de Suplementos</h2>
    <div class="grid">
      <div class="card">
        <img src="https://a-static.mlcdn.com.br/800x560/whey-protein-nutri-integralmedica-900g-baunilha/magazineluiza/087204200/336a1f9d9036e77bfddf1facc7164435.jpg" alt="Whey">
        <h3>Whey Protein</h3>
        <p>Recupere seus músculos com proteína de qualidade. R$129,90</p>
      </div>
      <div class="card">
        <img src="https://acdn-us.mitiendanube.com/stores/002/218/616/products/crea1-abd8ff086c388782e017183634041853-1024-1024.webp" alt="Creatina">
        <h3>Creatina</h3>
        <p>Aumente sua força e explosão nos treinos. R$89,90</p>
      </div>
      <div class="card">
        <img src="https://http2.mlstatic.com/D_NQ_NP_715106-MLA80057005672_102024-O.webp" alt="Pre-treino">
        <h3>Pré-Treino</h3>
        <p>Energia máxima com foco total. R$99,90</p>
      </div>
    </div>
  </section>

  <section class="container" id="imc">
    <h2>Calculadora de IMC</h2>
    <div class="imc-container">
      <p>Digite seu peso e altura para calcular o IMC:</p>
      <input type="number" id="peso" placeholder="Peso (kg)">
      <input type="number" id="altura" placeholder="Altura (m)">
      <br />
      <button onclick="calcularIMC()">Calcular</button>
      <p id="resultado"></p>
    </div>
  </section>

  <footer>
    <p>© 2025 Academia Cruzmaltina - Todos os direitos reservados</p>
  </footer>

  <script>
    function calcularIMC() {
      const peso = parseFloat(document.getElementById('peso').value);
      const altura = parseFloat(document.getElementById('altura').value);
      const resultado = document.getElementById('resultado');

      if (peso > 0 && altura > 0) {
        const imc = peso / (altura * altura);
        let classificacao = '';
        if (imc < 18.5) classificacao = 'Abaixo do peso';
        else if (imc < 24.9) classificacao = 'Peso normal';
        else if (imc < 29.9) classificacao = 'Sobrepeso';
        else if (imc < 34.9) classificacao = 'Obesidade grau I';
        else if (imc < 39.9) classificacao = 'Obesidade grau II';
        else classificacao = 'Obesidade grau III';

        resultado.innerText = `Seu IMC é ${imc.toFixed(2)} - ${classificacao}`;
      } else {
        resultado.innerText = 'Por favor, preencha os dados corretamente.';
      }
    }
  </script>
</body>
</html>
    """
    return HttpResponse(html)

