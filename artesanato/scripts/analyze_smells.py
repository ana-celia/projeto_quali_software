#!/usr/bin/env python3
"""
Script simplificado para análise de code smells.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def run_command(cmd, cwd=None):
    """Executa comando e retorna resultado."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

def print_header(title):
    """Imprime cabeçalho formatado."""
    print(f"\n{'='*60}")
    print(f"📊 {title}")
    print(f"{'='*60}")

def main():
    """Função principal."""
    print("🚀 ANÁLISE DE CODE SMELLS - VERSÃO SIMPLIFICADA")
    print("="*60)
    
    # Configurar
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
                    code = parts[3].strip().split()[0]
                    counts[code] = counts.get(code, 0) + 1
        
        print(f"🔍 Total de issues: {len(issues)}")
        print(f"📈 Issues por tipo:")
        for code, count in sorted(counts.items()):
            print(f"  • {code}: {count}")
        
        # Mostrar os principais
        print(f"\n🎯 PRINCIPAIS ISSUES:")
        for i, line in enumerate(issues[:10]):  # Mostrar apenas 10
            print(f"  {i+1}. {line}")
        
        if len(issues) > 10:
            print(f"  ... e mais {len(issues) - 10} issues")
    else:
        print("✅ Nenhum problema encontrado pelo Pylint!")
    
    # 2. ANÁLISE RADON
    print_header("2. ANÁLISE DE COMPLEXIDADE (RADON)")
    
    cmd = ["radon", "cc", "api/", "-a"]
    stdout, stderr, code = run_command(cmd)
    
    if stdout:
        # Contar notas
        grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        complex_items = []
        
        for line in stdout.split('\n'):
            if ' - ' in line:
                grade = line.split(' - ')[1].strip()
                if grade in grades:
                    grades[grade] += 1
                if grade in ['C', 'D', 'E', 'F']:
                    complex_items.append(line.strip())
        
        print("📊 Distribuição de notas:")
        for grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            count = grades[grade]
            if count > 0:
                icon = "🟢" if grade in ['A', 'B'] else "🟡" if grade == 'C' else "🔴"
                print(f"  {icon} Nota {grade}: {count}")
        
        if complex_items:
            print(f"\n⚠️  Itens complexos (notas C-F): {len(complex_items)}")
            for item in complex_items[:5]:
                print(f"  • {item}")
            if len(complex_items) > 5:
                print(f"  ... e mais {len(complex_items) - 5}")
        else:
            print("✅ Nenhum item complexo encontrado!")
    else:
        print("❌ Nenhum resultado do Radon")
    
    # 3. RESUMO DOS CODE SMELLS
    print_header("3. RESUMO DOS CODE SMELLS ENCONTRADOS")
    
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
        
        # Mostrar exemplos
        print(f"\n🎯 EXEMPLOS (máx 5 por categoria):")
        shown = 0
        for line in lines:
            if shown < 15:  # Mostrar até 15 exemplos
                print(f"  {line}")
                shown += 1
    else:
        print("✅ Nenhum code smell crítico encontrado!")
    
    # 4. RECOMENDAÇÕES
    print_header("4. RECOMENDAÇÕES PARA CORREÇÃO")
    
    issues_found = False
    
    # Verificar problemas específicos
    cmd = ["pylint", "--load-plugins", "pylint_django", 
           "--disable=all", "--enable=R0901", "api/"]
    stdout, stderr, code = run_command(cmd)
    
    if stdout.strip():
        print("🔴 1. PROBLEMA: Too many ancestors (R0901)")
        print("   • Seus ViewSets herdam muitas classes (11 > limite 7)")
        print("   • SOLUÇÃO: Criar ViewSet base comum")
        print(f"   • ENCONTRADO: {stdout.count('R0901')} ocorrências")
        issues_found = True
    
    cmd = ["pylint", "--load-plugins", "pylint_django", 
           "--disable=all", "--enable=C0301", "api/"]
    stdout, stderr, code = run_command(cmd)
    
    if stdout.strip():
        print("\n🔴 2. PROBLEMA: Linhas muito longas (C0301)")
        print("   • Linhas com mais de 100 caracteres")
        print("   • SOLUÇÃO: Quebrar linhas ou ajustar limite")
        print(f"   • ENCONTRADO: {stdout.count('Line too long')} ocorrências")
        issues_found = True
    
    cmd = ["pylint", "--load-plugins", "pylint_django", 
           "--disable=all", "--enable=C0103", "api/"]
    stdout, stderr, code = run_command(cmd)
    
    if stdout.strip():
        print("\n🟡 3. PROBLEMA: Nomes inválidos (C0103)")
        print("   • Nomes de migrations não seguem snake_case")
        print("   • SOLUÇÃO: Configurar Pylint para ignorar migrations")
        print(f"   • ENCONTRADO: {stdout.count('invalid-name')} ocorrências")
        issues_found = True
    
    if not issues_found:
        print("✅ Nenhum problema crítico encontrado!")
    
    print("\n" + "="*60)
    print("✅ ANÁLISE CONCLUÍDA")
    print("="*60)
    
    # Retornar código baseado em se encontrou issues
    if issues_found:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()