class Disciplina {
    constructor(nome, codigo) {
        this.nome = nome;
        this.codigo = codigo;
        this.alunosMatriculados = [];
    }

    matricularAluno(aluno) {
        if (aluno && aluno.nome && aluno.matricula) {
            this.alunosMatriculados.push(aluno);
            console.log(`Aluno ${aluno.nome} matriculado na disciplina ${this.nome}.`);
        } else {
            console.log("Aluno inválido. O aluno deve ter um nome e uma matrícula.");
        }
    }

    gerarBoletim() {
        if (this.alunosMatriculados.length === 0) {
            console.log(`Não há alunos matriculados na disciplina ${this.nome}.`);
            return;
        }
        console.log(`Boletim da disciplina ${this.nome} (Código: ${this.codigo}):`);
        this.alunosMatriculados.forEach(aluno => {
            console.log(`Nome: ${aluno.nome}, Matrícula: ${aluno.matricula}`);
        });
    }
}

const disciplina1 = new Disciplina("Matemática", "MAT101");

const aluno1 = { nome: "jair Messias", matricula: "123456" };
const aluno2 = { nome: "Michelle Bolsonaro", matricula: "654321" };

disciplina1.matricularAluno(aluno1);
disciplina1.matricularAluno(aluno2);
disciplina1.gerarBoletim();
