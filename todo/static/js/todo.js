    Vue.component('todo-item')

    var app = new Vue({
        delimiters: ['[[', ']]'],
        el: '#todolist',
        data: {
            tasks: [],
            description: '',
            edit: false,
            active: true
        },
        mounted() {
            axios.get('api/v1/tasks/').then(response => { this.tasks = response.data })
        },
        methods: {

            doneTask: function(index, id, description) {
                this.tasks[index].done = true
                
                axios.put('api/v1/tasks/' + id + '/', { description: description, done: true })
            },
            undoneTask: function(index, id, description) {
                this.tasks[index].done = false
                axios.put('api/v1/tasks/' + id + '/', { description: description, done: false })
            },
            deleteTask: function(index, id) {
                console.log('oi')
                this.tasks.splice(index, 1)
                axios.delete('api/v1/tasks/' + id + '/')
            },
            addTask: function(description) {
                if (description == ''){
                    return
                }

                if (this.tasks.length > 0){
                    length = this.tasks[this.tasks.length-1].index + 1 || 0;
                }
                else{
                    length = 1;
                }
                
                this.tasks.push({ description: description, index: length+1 })
                axios.post('api/v1/tasks/', { description: description, index: length })
                .then(function (response) {
                    location.reload();
                  }).catch(function (error) {
                    alert('Não foi possível salvar')
                  });

            },
            editTask: function(id, description, index) {
                axios.put('api/v1/tasks/' + id + '/', { description: description, index: index })
                .then(function (response) {
                    location.reload();
                  }).catch(function (error) {
                    alert('Não foi possível salvar')
                  });

            }
        }
    })
