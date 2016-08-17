

function minhaFuncao1()
{
    $('#area-01').css({
        color: '#ff0000',
        textTransform: 'uppercase',
        width: 600
        //width: '70%'
    });
};

function minhaFuncao2(){
    $('#area-02').empty();

    var alunos = ['Aluno 01 ', 'Aluno 02 ', 'Aluno 03 ', 'Aluno 04 ', 'Aluno 05 '];

    //$.each(alunos, function(index, value){
    //    $('#area-02').append("FELIPEARROMBADO").append(value);
    //});

    for(i = 0; i < alunos.length; i++)
    {
        $('#area-02').append(alunos[i]);
    }
};

function minhaFuncao3(){
    $('#area-02').empty();

    var alunos = [
      {
        nome: 'Aluno 01',
        idade: 11
      },

      {
        nome: 'Aluno 02',
        idade: 25
      },

      {
        nome: 'Aluno 03',
        idade: 32
      },

      {
        nome: 'Aluno 04',
        idade: 999
      }
    ];

    for(i = 0; i < 4; i++)
    {
        console.log(alunos[i]);
    }

    var list = $("#area-02").append('<ul></ul>').find('ul');
    $.each(alunos, function(index, value){
        list.append('<li>' + value.name + ' - ' + value.idade + '</li>');
    });
};
