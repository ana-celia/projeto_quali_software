#!/usr/bin/env python3
"""
Script para análise visual de code smells no projeto.
"""

import subprocess
from collections import defaultdict


def run_command(cmd, cwd=None):
    """Executa comando e retorna resultado."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1


def print_header(title):
    """Imprime cabeçalho formatado."""
    print(f"\n{'=' * 60}")
    print(f"📊 {title}")
    print(f"{'=' * 60}")


def main():
    """Função principal."""
    print("🚀 ANÁLISE DE CODE SMELLS - VERSÃO SIMPLIFICADA")
    print("=" * 60)
    
    # Configurar
    import os
    os.chdir("artesanato")
    
    # 1. ANÁLISE PYLINT COMPLETA
    print_header("1. ANÁLISE PYLINT COMPLETA")
    
    cmd = ["pylint", "--load-plugins", "pylint_django", "api/"]
    stdout, stderr, code = run_command(cmd)
    
    if code != 0:
        lines = stdout.split('\n')
        issues = [line for line in lines if ':' in line and line.strip()]
        
        # Contar por tipo
        counts = {}
        for line in issues:
            if ':' in line:
                parts = line.split(':')
                if len(parts) >= 4:
                    code_smell = parts[3].strip().split()[0]
                    counts[code_smell] = counts.get(code_smell, 0) + 1
        
        print(f"🔍 Total de issues: {len(issues)}")
        print(f"📈 Issues por tipo:")
        for code_smell, count in sorted(counts.items()):
            print(f"  • {code_smell}: {count}")
        
        # Mostrar os principais
        print(f"\n🎯 PRINCIPAIS ISSUES:")
        for i, line in enumerate(issues[:10]):
            print(f"  {i + 1}. {line}")
        
        if len(issues) > 10:
            print(f"  ... e mais {len(issues) - 10} issues")
    else:
        print("✅ Nenhum problema encontrado pelo Pylint!")
    
    # 2. RESUMO DOS CODE SMELLS
    print_header("2. RESUMO DOS CODE SMELLS")
    
    # Executar Pylint com filtro para code smells
    cmd = ["pylint", "--load-plugins", "pylint_django",
           "--disable=all",
           "--enable=R09,C01,C03,W06,E04", "api/"]
    stdout, stderr, code = run_command(cmd)
    
    if stdout.strip():
        lines = [l for l in stdout.split('\n') if l.strip()]
        
        # Agrupar
        categories = {
            'R09': 'Problemas de Design',
            'C01': 'Convenções',
            'C03': 'Formatação',
            'W06': 'Avisos',
            'E04': 'Erros de Import'
        }
        
        category_counts = {cat: 0 for cat in categories}
        
        for line in lines:
            for prefix in categories:
                if f":{prefix}" in line:
                    category_counts[prefix] += 1
        
        print("📋 Categorias de Code Smells:")
        for prefix, desc in categories.items():
            count = category_counts[prefix]
            if count > 0:
                print(f"  • {desc} ({prefix}): {count} issues")
        
        print(f"\n🔍 Total de code smells: {sum(category_counts.values())}")
    else:
        print("✅ Nenhum code smell crítico encontrado!")
    
    print("\n" + "=" * 60)
    print("✅ ANÁLISE CONCLUÍDA")
    print("=" * 60)


if __name__ == "__main__":
    main()
