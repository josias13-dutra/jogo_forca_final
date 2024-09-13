from django.urls import *
from .views import *

urlpatterns = [
    path("", TemaListView.as_view(), name="temaListPage"),
    path('tema/<int:pk>/', TemaDetailView.as_view(), name='temaDetalhes'),
    path('tema/<int:pk>/jogar/', ForcaGameView.as_view(), name='forcaPage'),
    path('win/', WinPageView.as_view(), name='winPage'),
    path('lose/', LosePageView.as_view(), name='losePage'),
    
        path("professor/pagina-geral", ProfessorGeralPageView.as_view(), name="professorGeralPage"),
    path("professor/tema/administrar-temas", AdministrarTemasPageView.as_view(), name="administrarTemasPage"),
    path("professor/tema/<int:pk>/editar/", EditarTemaPageView.as_view(), name="editarTema"),
    path("professor/tema/<int:pk>/deletar/", DeletarTemaPageView.as_view(), name="deletarTema"),
    
    path('professor/relatorio-atividade/', RelatorioAtividadeView.as_view(), name='relatorioAtividade'),

    path('professor/palavras/administrar-palavras', AdministrarPalavrasPageView.as_view(), name='administrarPalavrasPage'),
    path('professor/palavra/editar-palavra/<int:pk>/', EditarPalavraPageView.as_view(), name='editarPalavra'),
    path('professor/palavra/deletar-palavra/<int:pk>/', DeletarPalavraPageView.as_view(), name='deletarPalavra'),
]